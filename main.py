from processes.application_process import *


if __name__ == '__main__':
    inserts = {}
    # TODO: Should be Object("Universal Credit account") (see https://www.gov.uk/sign-in-universal-credit)
    # That won't work for now but we'll be able to fix it in the future
    for title in [[Verb("Apply"), "for", Object("Universal Credit")], [Verb("Sign in"), "to", "your", Object("Universal Credit")]]:
        for process in [BeginApplicationProcess(title), SignIn(title)]:
            if process.is_described():
                if not process.object() in inserts:
                    inserts[process.object()] = process
                else:
                    inserts[process.object()].link_to(process, preceeding=True, following=True)
    print("Done")

