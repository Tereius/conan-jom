#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class JomConan(ConanFile):
    name = "jom"
    version = "1.1.3"
    description = "jom is a clone of nmake to support the execution of multiple independent commands in parallel"
    url = "https://github.com/Tereius/conan-jom"
    homepage = "https://developer.android.com/studio/releases/sdk-tools"
    license = "Apache 2.0"
    settings = {"os": ["Windows"]}

    def source(self):
        source_url = "http://download.qt.io/official_releases/jom/jom_%s.zip" % self.version.replace(".", "_")
        tools.get(source_url)

    def package(self):
        self.copy("*.exe")
        self.copy("*.xml")
        self.copy("*.bat")

    def package_info(self):
        self.output.info('Appending PATH environment variable: %s' % self.package_folder)
        self.env_info.PATH.append(self.package_folder)
