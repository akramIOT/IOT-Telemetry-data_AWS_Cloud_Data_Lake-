Contributing Code
-----------------
A good pull request  with all details:


- Is the  MQTT  Client running on  Cisco IOT  gateway or some other  hardware
- Is  Cisco Edge intelligence /EI software used - version, IOT gateway Platform IOS or IOS-XE Version.
- Name/type of  hardware, version of  MQTT (3.x or  5.x), OS  type etc.
-  Is clear.
-  Works across all supported versions of Python.
-  Follows the existing style of the code base (see Codestyle section).
-  Has comments included as needed.

-  A test case that demonstrates the previous flaw that now passes with
   the included patch, or demonstrates the newly added feature.
-  If it adds/changes a public API, it must also include documentation
   for those changes.
-  Must be appropriately licensed (Apache 2.0).

Reporting An Issue/Feature
--------------------------
First, check to see if there's an existing issue/pull request for the
bug/feature. All issues are at


If there isn't an existing issue there, please file an issue. The
ideal report includes:

-  A description of the problem/suggestion.
-  How to recreate the bug.
-  If relevant, including the versions of your:

   -  Python interpreter
   -  Boto3
   -  Optionally of the other dependencies involved (e.g. Botocore)

-  If possible, create a pull request with a (failing) test case
   demonstrating what's wrong. This makes the process for fixing bugs
   quicker & gets issues resolved sooner.
