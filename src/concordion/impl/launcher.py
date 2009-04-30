

class TestLauncher:
    def __init__(self, xml_server, test_launcher):
        self.xml_server = xml_server
        self.test_launcher = test_launcher
    
    def launch(self, tests):
        for (python_file, java_class) in tests:
            self.xml_server.launch(python_file)
            self.test_launcher.launch(java_class)
            self.xml_server.stop()