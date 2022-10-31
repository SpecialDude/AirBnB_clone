#!/usr/bin/env python3

"""Entry point of the AirBnB clone"""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """AirBnB console: Entry point"""

    intro = 'Welcome to the AirBnB Console.   '\
        'Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    models = {

    }

    def emptyline(self):
        """Do nothing on emptyline input"""

        pass

    def do_quit(self, arg):
        """Exit the intepreter"""

        raise SystemExit

    def do_EOF(self, arg):
        """EOF handle"""

        self.do_quit(arg)

    def do_help(self, arg: str):
        """Help for the interpreter"""

        return super().do_help(arg)

    def do_create(self, arg):
        """Creates a new Model instance and saves it"""

        if arg == "":
            print("** class name missing **")
        else:
            cls = self.__get_model(arg)

            if cls is None:
                print("** class doesn't exist **")
                return

            cls = eval(arg)
            new_model = cls()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """Shows details of a model instance"""

        if arg == "":
            print("** class name missing **")
            return

        args = arg.split()
        cls_name = args[0]

        if not self.__model_exists(cls_name):
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]

        query_id = "{}.{}".format(cls_name, instance_id)

        instance = storage.all().get(query_id)

        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_delete(self, arg):
        """deletes a model instance"""

        if arg == "":
            print("** class name missing **")
            return

        args = self.__parse_argument(arg)
        cls_name = args[0]

        if not self.__model_exists(cls_name):
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]

        query_id = "{}.{}".format(cls_name, instance_id)

        try:
            storage.all().pop(query_id)
            storage.save()
        except KeyError as err:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all model instance"""

        if arg == "":
            print("** class name missing **")
        else:
            if not self.__model_exists(arg):
                print("** class doesn't exist **")
                return

            models = [
                str(model) for id, model in storage.all().items()
                if id.startswith(arg)
            ]
            print(models)

    def do_update(self, arg):
        """updates a model instance"""

        if arg == "":
            print("** class name missing **")
            return

        args = self.__parse_argument(arg)
        cls_name = args[0]

        if not self.__model_exists(cls_name):
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]

        query_id = "{}.{}".format(cls_name, instance_id)

        instance = storage.all().get(query_id)

        if instance is None:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        attr = args[2]

        if len(args) == 3:
            print("** value missing **")
            return

        value = args[3]

        if attr not in ("created_at", "updated_at", "id"):
            attr_type = getattr(instance, attr).__class__
            value = attr_type(value)
            setattr(instance, attr, value)
            instance.save()

    def __get_model(self, model_name):
        """Returns a model cls"""

        try:
            cls = eval(model_name)
            return cls
        except NameError as err:
            return None

    def __model_exists(self, model_name):
        """Checks if model exists"""

        return self.__get_model(model_name) is not None

    def __parse_argument(self, arg):
        """Parses a string argument and returns as a list"""

        return shlex.split(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
