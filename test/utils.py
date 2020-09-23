def create_election_test_message():
  return {
    "scheme": {
      "name": "electionguard",
      "parameters": { "quorum": 2 }
    },
    "trustees": [
      { "name": "alicia", "public_key": "..." },
      { "name": "bob", "public_key": "..." },
      { "name": "clara", "public_key": "..." },
      { "name": "david", "public_key": "..." }
    ],
    "description": {
      "name": { "text": [{ "value": "Test election", "language": "en" }]},
      "start_date": "2021-03-01T08:00:00-05:00",
      "end_date": "2021-03-01T20:00:00-05:00",
      "candidates": [
        { "object_id": "question1-yes", "ballot_name": { "text": [{ "value": "Yes", "language": "en" }]}},
        { "object_id": "question1-no", "ballot_name": { "text": [{ "value": "No", "language": "en" }]}},
        { "object_id": "question2-first-project", "ballot_name": { "text": [{ "value": "First project", "language": "en" }]}},
        { "object_id": "question2-second-project", "ballot_name": { "text": [{ "value": "Second project", "language": "en" }]}},
        { "object_id": "question2-third-project", "ballot_name": { "text": [{ "value": "Third project", "language": "en" }]}},
        { "object_id": "question2-fourth-project", "ballot_name": { "text": [{ "value": "Fourth project", "language": "en" }]}}
      ],
      "contests": [
        {
          "@type": "ReferendumContest",
          "object_id": "question1",
          "sequence_order": 0,
          "vote_variation": "one_of_m",
          "name": "Question 1",
          "number_elected": 1,
          "minimum_elected": 1,
          "ballot_title": { "text": [{ "value": "Do you agree?", "language": "en" }]},
          "ballot_subtitle": { "text": [{ "value": "Choose 'Yes' or 'No'", "language": "en" }]},
          "ballot_selections": [
            { "object_id": "question1-yes-selection", "sequence_order": 0, "candidate_id": "question1-yes" },
            { "object_id": "question1-no-selection", "sequence_order": 1, "candidate_id": "question1-no" }
          ]
        },
        {
          "@type": "CandidateContest",
          "object_id": "question2",
          "sequence_order": 1,
          "vote_variation": "n_of_m",
          "name": "Question 2",
          "number_elected": 2,
          "minimum_elected": 0,
          "ballot_title": { "text": [{ "value": "Choose the projects that you like", "language": "en" }]},
          "ballot_subtitle": { "text": [{ "value": "You can select at most two projects", "language": "en" }]},
          "ballot_selections": [
            { "object_id": "question2-first-project-selection", "sequence_order": 0, "candidate_id": "question2-first-project" },
            { "object_id": "question2-second-project-selection", "sequence_order": 1, "candidate_id": "question2-second-project" },
            { "object_id": "question2-third-project-selection", "sequence_order": 2, "candidate_id": "question2-third-project" },
            { "object_id": "question2-fourth-project-selection", "sequence_order": 3, "candidate_id": "question2-fourth-project" }
          ]
        }
      ]
    }
  }

def joint_election_key_test_message():
  return {
    "joint_election_key": 347509845823288811287955580035367375509528249324522433746382543335997721752502454213077251056881169843561932095668985758469224311674449026375506609936237946412146111615288804937317208881952627098524961594259299389780312095616700923727069935957910154473750066624489508536859377589510189998717757905602774778405338812988588654565056619339455806481785915727042572763533601111739917875740840936712892003131176189596293615241679535724659695213145310900078258082511585786408979431097091754446843386117481121924407947814523538959200864634936595122615809926796486671188598891269534578565162284629918459899011326861496252640355264234876423782782792254297842324502481400125231754048551565803216760525766606997963399615487131372287828656179674246440755977596157194206281625344003385599877681492506652767716885642026178241756326882200567694842164589422327344804292387060066533626102218079434051917084846436290350628537239873029687040558991165515684864777834876188539993452864785432376184265419962265729790706356681129127424545869353404712966114942349931600478134713592076637759923822958038371253855633150263348696355214006650514828509472559182197086060164910617049820754502465930552816494484513467714823750599910951652964408107186727779826474539
  }
