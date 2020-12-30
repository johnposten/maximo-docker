"""
   Copyright Yasutaka Nishimura 2017, 2019

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


def load_wsadminlib(filename):
    global enableDebugMessages, listAllAppServers, startServer
    exec(open(filename).read())


filename = '/work/wsadminlib.py'
# Try execfile first for Jython
try:
    execfile(filename)
except NameError:
    load_wsadminlib()

enableDebugMessages()
for (nodename, servername) in listAllAppServers():
    startServer(nodename, servername)
