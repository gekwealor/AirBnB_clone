#!/usr/bin/python3
"""Line_oriented command imterpreters written"""
import cmd
import sys
import json
from models import *
from models import storage
import re


class HBNBCommand(cmd.Cmd):

	"""Writting a simple line-oriented command"""
	prompt = "(hbnb) "


	def do_EOF(self, line):
	    """Should quit command to exit the program\n"""
	    return True

	def emptyline(self):
	    """Return empty when line is called"""
   	    if self.lastcmd:
	        self.lastcmd = ""
	        return self.onecmd('\n')

	def do_create(self,line):
	    """Usage:create<class_name>,Function:instance of class to be created"""
	    if line != "" and line is not None:
	        if line not in storage.classes():
			print("** class fails to exist **")
		else:
		    # Instance of the given class to be created
		 new_obj.save()
		 new_obj = storage.classes()[line]()
		 print(new_obj.id)
	    else:
	        print("** missing class name **")

		def do_show(self, line):
        """Usage: show <class_name> <id>
           Funtion: shows object at given id
        """
        args = line.split(" ")
        if len(args) == 0 or args[0] == '' or args[0] is None:
            print("** missing class name **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** missing instance id **")
        else:
            instance_id = args[1]
            class_name = args[0]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no found instance **")

    def do_destroy(self, line):
        """Usage: destroy <class_name> <id>
           Funtion: deletes object at given id
        """
        args = line.split(" ")
        if len(args) == 0 or args[0] == '' or args[0] is None:
            print("** missing class name **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** missing instance id **")
        else:
            instance_id = args[1]
            class_name = args[0]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                del (storage.all()[key])
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints instances of all string representation.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """Instances of a class counted.
        """
        words = line.split(' ')
        if not words[0]:
            print("** missing class name **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """An instance by adding or updating attribute updates.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** missing class name **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** missing id instance **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** missing name attributes **")
            elif not value:
                print("** missing value **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBcommand().cmdloop()
