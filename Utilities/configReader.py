from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
#
# print(config.get("locator","username"))
# print(config.get("basic info","testsiteurl"))
# print(config.get("locator-userreg","firstname"))


def readConfig(section,key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\conf.ini")
    return config.get(section,key)

# print(readconfig("locators","username"))
# print(readconfig("basic info","firstname"))