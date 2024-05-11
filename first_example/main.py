import sys
import flask

print("Hello from inside a container!")
print(f"Version of Python: {sys.version}")
print(f"Version of Flask: {flask.__version__}")
