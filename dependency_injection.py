'''
"Dependency injection is basically providing the objects that an object needs (its dependencies) instead of having it construct them itself.
It's a very useful technique for testing, since it allows dependencies to be mocked or stubbed out." - https://stackoverflow.com/questions/130794/what-is-dependency-injection

It allows for flexible configuration of the class by the client that calls it.

Using dependency injection is advantageous because it decreases coupling - otherwise, a class would explicitly
depend on another, so if the class depending on the other on initialization needs different behavior, they're out of luck.

Oftentimes, specialized frameworks are used for DI, because it can create a lot of boilerplate also when
explicitly injecting dependencies:
    "On the other hand, using a framework makes it easier, particularly one based on annotations or automatic detection of dependencies,
    as it makes the process simpler: if I decide that I need a new dependency in a class,
    all I have to do is add it to the constructor (or declare a setter) and the object is injected -
    I don't need to change any instantiation code." - https://softwareengineering.stackexchange.com/questions/300127/why-do-we-need-frameworks-for-dependency-injection

'''

# taken from https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html

import os


class ApiClient:

    def __init__(self, api_key: str, timeout: int) -> None:
        self.api_key = api_key  # <-- dependency is injected
        self.timeout = timeout  # <-- dependency is injected


class Service:

    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client  # <-- dependency is injected


def main(service: Service) -> None:  # <-- dependency is injected
    ...


if __name__ == "__main__":
    main(
        service=Service(
            api_client=ApiClient(
                api_key=os.getenv("API_KEY"),
                timeout=int(os.getenv("TIMEOUT")),
            ),
        ),
    )