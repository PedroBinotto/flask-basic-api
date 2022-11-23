from setuptools import setup

if __name__ == "__main__":
    setup(
        name="flaskbasicapi",
        version="1.0.0",
        description="Meta-framework for building Flask-based RESTful APIs",
        package_dir={"": "src"},
        packages=["flaskbasicapi", "flaskbasicapi.api"],
    )
