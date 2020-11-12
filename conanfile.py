from conans import ConanFile, CMake, tools

class IncppectConan(ConanFile):
    name = "incppect"
    version = "0.1"
    license = "MIT License"
    description = "Inspect C++ memory in the browser"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def requirements(self):
       self.requires("uwebsockets/18.3.0")

    def source(self):
        self.run("git clone ssh://git@bitbucket.seamlessme.local:7999/seamlessme/incppect.git -b xqp/use_conan")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="incppect")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/incppect", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["incppect"]
