#!/usr/bin/python

import os, sys
from impl.java import JavaClassGenerator, Classpath, JavaFileCompiler, JavaTestLauncher
from impl.configuration import FileConfiguration
from impl.executors import CommandExecutor
from impl.xmlrpc import XmlRpcServer
from impl.launcher import TestLauncher
from impl.files_finders import FolderTestFinder

if len(sys.argv) != 2:
    print "USAGE :", sys.argv[0], "tests_directory"
    sys.exit(1)

directory = sys.argv[1]
print directory
python_files = FolderTestFinder(directory).find_files()
print "Found files :", python_files
installation_path = os.path.split(__file__)[0]
config = FileConfiguration(os.path.join(installation_path, "config.ini"))
lib_path = os.path.join(installation_path, "lib")
classpath = Classpath(lib_path)

java_files = JavaClassGenerator().run(python_files)
print "Generated files :", java_files

executor = CommandExecutor()

java_class_filenames = JavaFileCompiler(config, classpath, executor).compile(java_files)

xmlRpcServer = XmlRpcServer(config)
java_launcher = JavaTestLauncher(config, classpath, executor)
python_and_java = []
for i in range(len(python_files)):
    python_and_java.append((python_files[i], java_class_filenames[i]))

TestLauncher(xmlRpcServer, java_launcher).launch(python_and_java)

for java_filename in java_files :
    os.remove(java_filename)
for java_class_filename in java_class_filenames:
    os.remove(java_class_filename)