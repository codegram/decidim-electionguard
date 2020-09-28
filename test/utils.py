def create_election_test_message():
    return {
        "scheme": {
            "name": "electionguard",
            "parameters": {"quorum": 2}
        },
        "trustees": [
            {"name": "alicia", "public_key": "..."},
            {"name": "bob", "public_key": "..."},
            {"name": "clara", "public_key": "..."}
        ],
        "description": {
            "name": {"text": [{"value": "Test election", "language": "en"}]},
            "start_date": "2021-03-01T08:00:00-05:00",
            "end_date": "2021-03-01T20:00:00-05:00",
            "candidates": [
                {"object_id": "question1-yes", "ballot_name": {"text": [{"value": "Yes", "language": "en"}]}},
                {"object_id": "question1-no", "ballot_name": {"text": [{"value": "No", "language": "en"}]}},
                {"object_id": "question2-first-project",
                    "ballot_name": {"text": [{"value": "First project", "language": "en"}]}},
                {"object_id": "question2-second-project",
                    "ballot_name": {"text": [{"value": "Second project", "language": "en"}]}},
                {"object_id": "question2-third-project",
                    "ballot_name": {"text": [{"value": "Third project", "language": "en"}]}},
                {"object_id": "question2-fourth-project",
                    "ballot_name": {"text": [{"value": "Fourth project", "language": "en"}]}}
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
                    "ballot_title": {"text": [{"value": "Do you agree?", "language": "en"}]},
                    "ballot_subtitle": {"text": [{"value": "Choose 'Yes' or 'No'", "language": "en"}]},
                    "ballot_selections": [
                        {"object_id": "question1-yes-selection", "sequence_order": 0, "candidate_id": "question1-yes"},
                        {"object_id": "question1-no-selection", "sequence_order": 1, "candidate_id": "question1-no"}
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
                    "ballot_title": {"text": [{"value": "Choose the projects that you like", "language": "en"}]},
                    "ballot_subtitle": {"text": [{"value": "You can select at most two projects", "language": "en"}]},
                    "ballot_selections": [
                        {"object_id": "question2-first-project-selection", "sequence_order": 0,
                            "candidate_id": "question2-first-project"},
                        {"object_id": "question2-second-project-selection", "sequence_order": 1,
                            "candidate_id": "question2-second-project"},
                        {"object_id": "question2-third-project-selection", "sequence_order": 2,
                            "candidate_id": "question2-third-project"},
                        {"object_id": "question2-fourth-project-selection", "sequence_order": 3,
                            "candidate_id": "question2-fourth-project"}
                    ]
                }
            ]
        }
    }


def joint_election_key_test_message():
    return {
        "joint_election_key": "0nOW5bz3DrLecByUXW2H/WsK87OyCSeUVJf8Y4Vn4q923ofId84xnfglP9Dbz7unATSCrfP6xpuJ3f8vk5occs4yvnv4HR83lqqP+/yyCajVqQLSgMTpUTi/lh5fA4qe7ndVbg5twOPNDgcHVCUTici6xh7hdPmVo92a6nP4AAmA8y1l8VqTF8WrWAPm1PeILHOTpj0xRhNhAeg/SYxIu61mmkJ2MNch/T0xDFk1YlcT4+WZzYkI+oGb41ZKtrmu5IpXBzbUf0YiRW/6MnqIK2VOf9sTRGLh+bK841KL9EPR4cNyoymP/kfvnoauHuHDuvclKClC0izGbUsovFG2cz/r6FjvelMt9eVc9ccNA0/grjM8whdkDYpQtaQynTHxMD3OCyqW2mcFEzFPWmhLP9kmRE43sBTCQtYdJ+lip+urpAw+y6+L1RraykGzg5NVhm2Pa8UV34522YB4lhsOU7b/Do9WdtvWxReY+HJOIMJwaROgybn0eV4v+E13q0WJDK31JA/o7IHIPGlRVbkcb6/0qrDbho0pCRgjQAtQ6i3JxRXpMDAEblWP5h38qJHQwpmIl9v9b1i5RVBge4LhxQXAAatvrZcPI4QZUmvtpXXJ7jP2KBGUbVmmsFKrmTO/7u76nydqmg3yFbDywfr9wg3PCLBUUx5WWil0TmVdeNE="  # noqa: E501
    }
