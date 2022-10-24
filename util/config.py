from configparser import ConfigParser

config = ConfigParser()
file = r"D:\myscript\games\cui\textbasedrpg\datastore\settings.cfg"
config["DEFAULT"] = {"Path": "C:/Test"}
with open(file, "w") as f:
    config.write(f)
config.read(file)
print(config["DEFAULT"]["PATH"])

# config.defaults()
# config.sections()
# config.add_section(section)
# config.has_section(section)
# config.options(section)
# config.has_option(section, option)
# config.read(filenames, encofing=None)
# config.read_file(f, source)
# config.read_string(string, source)
# config.read_dict(dictionary, source)
# config.get(section, option)
# config.getint(section, option)
# config.getfloat(section, option)
# config.getboolean(section, option)
# config.items(section)
# config.set(section, option, value)
# config.write(fileobject)
# config.remove_option(section, option)
# config.remove_section(section)