from processes.application_process import *
import sys
# Requires the govuk-entity-personalisation repository (https://github.com/alphagov/govuk-entity-personalisation)
# for subject-verb-object extraction
# Install the repo requirements to use
# This isn't ideal but it seems foolish to have the code in two places. If this project is promising it could get
# moved to that repo or vice versa
sys.path.append('../govuk-entity-personalisation/')
from src.make_features.subject_verb_object.content import Title
from src.make_features.subject_verb_object.utils import spacy_model

if __name__ == '__main__':
    inserts = {}
    # TODO: Should be Object("Universal Credit account") (see https://www.gov.uk/sign-in-universal-credit)
    # That won't work for now but we'll be able to fix it in the future
    nlp = spacy_model()
    for page_title in ["Apply for Universal Credit", "Sign in to your Universal Credit"]:
        title = Title(page_title, nlp)
        for triple in title.subject_object_triples():
            recast_triple = [Subject(triple.cypher_subject()), Verb(triple.cypher_verb()), Object(triple.cypher_object())]
            for process in [BeginApplicationProcess(recast_triple), SignIn(recast_triple)]:
                if process.is_described():
                    if not process.object() in inserts:
                        inserts[process.object()] = [process]
                    else:
                        inserts[process.object()][0].link_to(process, preceeding=True, following=True)
                        inserts[process.object()].append(process)
    apply = inserts['universal credit'][0]
    log_in = inserts['universal credit'][1]
    assert apply.has_link_to(log_in, following=True)
    assert log_in.has_link_to(apply, preceeding=True)
    print("Done")

