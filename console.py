#!/usr/bin/python3
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
"""
This module contains declaration of command line interpreter for
AirBnB project
"""


class HBNBCommand(cmd.Cmd):
    """ class for command line interpreter """

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "Amenity",
                 "City", "Place", "Review", "State"]
    __methods = ["all", "create", "update", "show", "destroy"]

    def command_errors(self, line, num_of_args):
        """command_errors: detector for errors in command line args

        Args:
            line (str): command line arguemnts
            num_of_args (int): number of command line args

        Returns:
            boolean: True if no errors in command line, False otherwise
        """
        if not line:
            print("** class name missing **")
            return False

        args = line.split(" ")
        if num_of_args >= 1 and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return False
        elif num_of_args == 1:
            return True
        if num_of_args >= 2 and len(args) < 2:
            print("** instance id missing **")
            return False
        dictionary = storage.all()
        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if 2 <= num_of_args and key not in dictionary:
            print("** no instance found **")
            return False
        if num_of_args >= 3 and len(args) < 3:
            print("** attribute name missing **")
            return False
        if num_of_args >= 4 and len(args) < 4:
            print("** value missing **")
            return False
        return True

    def do_create(self, line):
        """create: create new instance of
        the class argument passed to the command

        Args:
            line (str): command line arguemnt represent
            class name to be created
        """
        args = line.split(" ")
        if self.command_errors(line, 1) is False:
            return
        newobj = eval(args[0])()
        newobj.save()
        print(newobj.id)

    def do_show(self, line):
        """do_show: command to show instace of a class from saved classes
        using class id as a reference to the class to be shown

        Args:
            line (str): command line arguments provided to show command
        """
        if self.command_errors(line, 2) is False:
            return
        args = line.split(" ")
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        obj = storage.all()
        print(obj[args[0] + '.' + args[1]])

    def do_destroy(self, line):
        """do_destroy: command to remove instace of a class from saved classes
        using class id as a reference to the class to be shown

        Args:
            line (str): command line arguments provided to delete command
        """
        if self.command_errors(line, 2) is False:
            return
        args = line.split(" ")
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        obj = storage.all()
        del obj[args[0] + '.' + args[1]]
        storage.save()

    def do_all(self, line):
        """do_all: command to all instances of any class we have in system

        Args:
            line (str): command line arguments provided to get only instaces
            for specifiec class using all <class_name>
        """
        dicts = storage.all()
        if not line:
            print([str(val) for val in dicts.values()])
            return
        args = line.split(" ")

        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        else:
            print([str(val) for val in dicts.values()
                  if val.__class__.__name__ == args[0]])

    def do_update(self, line):
        """do_update: command to update instance of any class
        with specific attrs

        Args:
            line (str): command line arguments provided to update
            instace with specifiec id only with specifiec value updated to
            specifiec attribute
            and also it can be used to add custom attributes to the class attrs
        """
        if self.command_errors(line, 4) is False:
            return
        args = line.split(" ")
        obj = storage.all()
        for i in range(len(args[1:]) + 1):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        attrs = obj[key].__dict__
        try:
            args[3] = type(attrs[args[2]])(args[3])
        except Exception:
            pass
        setattr(obj[key], args[2], args[3])
        storage.save()

    def do_quit(self, line):
        """quit: close command line interpreter

        Args:
            line (str): command line arguments provided to quit command

        Returns:
            booleans: true
        """
        return True

    def do_EOF(self, line):
        """EOF command: alias for quit

        Args:
            line (str): command line arguments provided to quit command

        Returns:
            booleans: true
        """
        return True

    def emptyline(self):
        return False

    def count(self, line: str):
        objs_count = 0
        if line not in self.__classes:
            print("** class doesn't exist **")
            return
        d = storage.all()
        for obj in d.values():
            if obj.__class__.__name__ == line:
                objs_count += 1
        print(objs_count)

    def default(self, line: str):

        commands = {
            "all": self.do_all,
            "create": self.do_create,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.count
        }

        args = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)

        if args:
            args = args.groups()
        if not args or len(args) < 2 \
           or args[1] not in commands.keys():
            super().default(line)
            return

        if args[1] in ["all", "count", "create"]:
            commands[args[1]](args[0])
        elif args[1] in ["show", "destroy"]:
            commands[args[1]](args[0] + ' ' + args[2])
        elif args[1] in ["update"]:
            updates = re.match(r"\"(.+?)\",(\s*)(.*)", args[2])
            if updates:
                updates = updates.groups()
            if len(updates) > 1 and updates[2][0] == '{':
                updates_dict = eval(updates[2])
                for k, v in updates_dict.items():
                    updated_str = f"{args[0]} {updates[0]} {k} {v}"
                    commands[args[1]](f"{updated_str}")
            else:
                updated_args = re.findall(r"(\w+)", updates[2])
                updated_str = " ".join([updates[0], *updated_args])
                commands[args[1]](f"{args[0]} {updated_str}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
