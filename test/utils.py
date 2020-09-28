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


def trustees_public_keys():
    return [
        {
            'owner_id': 'alicia',
            'sequence_order': 0,
            'auxiliary_public_key': '-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA6HhvGDSiKTN+Osb7m+Gt\nAKFzr00lrkN5PWvZXcQxO27VGe/007fH3w7okKszJdv4Rsc5Cu+Xf4F4EQhN2H3q\n9YT4Rck7KpnHX7RaktV8yhJb7O7+O6wLt9/AzLbHkGYJlnIJMHpG6bbL300kGmhI\nSqHzNikSTqJytkrjjgL3nL7AQXq6DGOzpn7DfIBlnZq6vdWDgT0Eqwc7FxPFHyxM\nYUBl86EjhPpvonfAVWlk9Wp55dpeXbI2JsI1uaJliQcJF5bWJcx03QbEMcvs4HUT\nBbku/qSklfuHc96ebGBMgzM7Qyp5DY5HWSg2x+tF0v5j1+ZALKrJcQgnNj3IaTzc\nG3prvjaWbUwdJLBkRD7Fz112ZatS0K/kbf17OZW254wFXuHx3/DCl0r/XXI4PFeR\nWzfGFga6OKRd5dJxpwVbJ38+t53IQPA94OIn/4Ly8n1KtKawzXwFg6+p1ALUAw/Y\nJiwOBeoVrt/ChMvl+fLLH5TLNnhFkF2C9Is2dM+Q0wEc9sTkIYT9TOGfDrIvJOk9\nO0LIdj/ojB9aNkZB6A90m1QtpjYRpza+OG3uMNsjC4xd7w28vjs6EQPK+eKcPQ44\nA/xoJoAZ735k9qMYRz9RCK52TqdTwWFUfvg+Rrh9g9s0I7tNNcgxUSYFY51WWL1+\n9VxP6xd8EJVFheoyHc6P5isCAwEAAQ==\n-----END PUBLIC KEY-----\n',  # noqa: E501
            'election_public_key': 'UxmYOgII7XfkqtmIhkm2I3W5g83recLynlu+z6qK9/iSyB1hW+H7j7KpKnd+pLAOCnxrKA7Kglxk4x5jQdXfYRhiTkL9TzIhejVoXpFFEqH8I1+8mPCYMPY1GxBhZodbAl3CRSIRqS7IMQfFZ6gtZFjrij5P70SuXYyI+K2igVcQuG1BK8CKFXpzDxiKhbVltIjNk4un8K48lTkNqH+nyJ+GQiBUi+x2/gGxgF6naQO9Z/ZAgTcECf9J7LnPxY/0iFkAyJsQiyDpktPCVfy5aAfUYwbDxatIIoE7ujKXyxrbEHPu+VtX3GvLRb53kPp8Wuh3b8eDSagwmh4Fa/yHpcfq1CJSGT4C4K55VbtQ1PcMTQyGJEtgBjpU/3XGyLK1TarnmFlZonKRiuYhHMLKmj4E1F5jaJ12/AwS+jXjTASZwMHgVdflkMCH/rceutcLTKtISNtZdGmP9JcnQ1uOCr1EQe/2sTlz1M8YzvupoPtBUE9ZtgvxGzPKx+tldJQv1cqVsAYTmEL3McUFeK3YLa5819kAOdZ/1tGy3pk3mIRdbiD1GFyiW3MEOwEAKVikIxninC0TwIw0ZiKh5C6YP3mOTN2C8zmWle1uPihO7XLK0f4TKC0pyCMXklkyZa05ZmjWgctJ17RWjLE1boNVTFwFOmy3ASErzDGbJtu9g8A=',  # noqa: E501
            'election_public_key_proof': {
                'challenge': '7ER1o3ZlShoCD8Okg5Q6uaUAJUpL1l7SdD4pg6CkAw8=',
                'commitment': 'pl8zhjfiBLMCm/IgqapjuvmiU0d1EmfOANkf+ld3+R+EqWLZQ0K4l3Ae3Dv3ipP2dgKqNv/wGe61ZoRvhFGkQJnxXo/nFH3OR9bwqZLHpv6ZYeSX3ajD/f+M7nFUCbxDyZvlZYcPLcr2LSgFPXyKDr9tqpazpkQBo44ztZDIe1llv+aaxoiJP/A36IO0bVGKDG2BEU99+qUPMk8rxzaahI3u7yhI8MOC2FJUWTWwTZgnWsV2DnduGaW2cipCG1mbs3OfqHTodl10rOeLngw9CyybfvZdp0YIv1WLGO6S5jadJBYhptUCpamLW0C5pVpCG8uvTaR28kKS9h0NqEu6qa8g5Ow5bKrfxV2vb9SH4Ut1+2+9HqPyjGN16jKMIT79ZCu1iEEN2+RUw9K0rdRaqhKcOY9imLeHk8L5D0GJpR5MYgluFCmDl/+YDZbzE/m165OPiirqlSpY9gn9jCflDuXx9gR/kqsw28z1ImYo7eBDRPG2tQGgExibhycK4SLxPBL3nvYwtlrvd0EtP7eyA6Wb1RotJ92snSH5J5SleNBNCFEWm6cnlGGJ5el/2/kG/jcDVXLz4V02s6+FTbWXTF6s9mOg9Jp65av/T2umlfWvgT/r72AGyOn4hQtI9aGdyv7xPxyU7iiZa2h7BUpEQ3R5F2CO8NmBpdS0m5VEfrA=',  # noqa: E501
                'name': 'Schnorr Proof',
                'public_key': 'UxmYOgII7XfkqtmIhkm2I3W5g83recLynlu+z6qK9/iSyB1hW+H7j7KpKnd+pLAOCnxrKA7Kglxk4x5jQdXfYRhiTkL9TzIhejVoXpFFEqH8I1+8mPCYMPY1GxBhZodbAl3CRSIRqS7IMQfFZ6gtZFjrij5P70SuXYyI+K2igVcQuG1BK8CKFXpzDxiKhbVltIjNk4un8K48lTkNqH+nyJ+GQiBUi+x2/gGxgF6naQO9Z/ZAgTcECf9J7LnPxY/0iFkAyJsQiyDpktPCVfy5aAfUYwbDxatIIoE7ujKXyxrbEHPu+VtX3GvLRb53kPp8Wuh3b8eDSagwmh4Fa/yHpcfq1CJSGT4C4K55VbtQ1PcMTQyGJEtgBjpU/3XGyLK1TarnmFlZonKRiuYhHMLKmj4E1F5jaJ12/AwS+jXjTASZwMHgVdflkMCH/rceutcLTKtISNtZdGmP9JcnQ1uOCr1EQe/2sTlz1M8YzvupoPtBUE9ZtgvxGzPKx+tldJQv1cqVsAYTmEL3McUFeK3YLa5819kAOdZ/1tGy3pk3mIRdbiD1GFyiW3MEOwEAKVikIxninC0TwIw0ZiKh5C6YP3mOTN2C8zmWle1uPihO7XLK0f4TKC0pyCMXklkyZa05ZmjWgctJ17RWjLE1boNVTFwFOmy3ASErzDGbJtu9g8A=',  # noqa: E501
                'response': 'puH3SmTJnSn4JL3uDM5exiB0mDa67vibiu3qkA8IbCM=',
                'usage': 'SecretValue'
            }
        }, {
            "owner_id": "bob",
            "sequence_order": 1,
            "auxiliary_public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAs14L9s38kkSVAB+uDJJP\nmRdIUACwYq/K9r/c/XJs5AnzMLMyxAASASz0c84Unyf5mEE3iE7N5zPw82fcmdh0\njDm+9vFTygEIm5qSE31ooVKilcg181vl2e4LsGO8oqXn0ZKUoOV1TVUSrjWOsuP8\nwQKyHr34Bw/c+wxvIbDsQa+9uFWXMWdkeAJNQqnGfq17oiVATIZmXfa/S8DMLoZm\noYLMyRv7Vb8TN4Q5mi7AnGocUL5V8nfZLm0970j8hDxlqK1mkxO+ZWwLuIO9NZhq\nATi3zdA4MKw7eiZXcj00EYHy48Nzt7n7l89xNM2eYdqJgoIy46SmoK5zHWwY3Fhf\nrW3DL3RRDL79FP2PaEx2olgb9IzGKmspCZMi43/PhQ39qmzyv8h979C1oD2qZnWT\nXyhpid1X4guUyegqlDQxG9KEhkt1FS3OPPkPewVPfqhCavBWDQaJaG8RgccBZ82z\nbcQuAVqEf9qPUUuTwpVbG5cxTvqV6pOstDc3dtEJxarHEEaY78iWq8K3tFpptlVA\n807YCfJPfZdp6qThBnkFcJROSAZSEa6sVcJyp4nOCk3Jyedcd76IpzeU7ueSRSho\nnyJsB9Eedtq2I7BsOolfngqe4pVaXorf5vcHkwpcNg0THYSvUuC4b6XEW8XqnT70\nMqKEUoA5ixoJ2pf9tXaVgYUCAwEAAQ==\n-----END PUBLIC KEY-----\n",  # noqa: E501
            "election_public_key": "7+o8hAuyqbgCBixFFyIxUim4sGgjsVhQVP0o10ohgBN5++f2ohuBvSbBb9VzKx4vmRzd7sfCxwpAeo+z/QQVmDHWLrcp17y/kYbipB3cE3ewsneojyh+qEqY5H9/QiRZkC2X3XVqPVxJv5aVS3Um4vFsfCgS6uWc6HxayWu0TOgQu5FNH4hQxQH7QI68u4uthuvyUfH0t7rqXgOoBbXpm3vPrJBnLvCaxL3FBUvQH27nW5prQoRFCjzUZgEJJtUbykIPWCI/VMT/Ui8jwx3EA8bsVwUti3Mdptlv9MilOlPKo7ChaNg/vzVqsmX2xKXGXhBijgG1iey+5FnIZPQBs/fCkHc9h13pVaEJemJDhZIhiYQ2KxDmf2bWk/ZR5LKX4kFpyY+MI3KSkK2HGrvFiLej2Wxc3jWUK3LmVBCxxB1JrAX94k5fOalVGA74cNte1dp644fR+7h/7K4huDfoVbqh+arkMfg1VDEnPCMjPuox+mwR0DfDvL1niOFNwSNuSdeFqRMdj0Fcx5vG4KXCZTDlPUQIcu9VwdQnXJWqf1izh7Ol2Oi4//Y+3PX8BzMUSyt3L1x2h8kC7sHvIVO+bA9zEjN105X0RJcLkP6WM/27MyrlcfSbWAD2LOBoXySTxiv0wBuDxowo/X2nW7nTcHqu2gaabeZQGMf8/F9VI/o=",  # noqa: E501
            "election_public_key_proof": {
                "challenge": "jTFR44h84a0/XwiKNwdtSDaTb3EYJjOuePX6uaYn2Ds=",
                "commitment": "hQXsT3tF9zhu5LcK4IFr8sTZmMXbkUMRXqFzlTUdV8ekcB/0ZwoC6zWcdia5BpSv4og2eIUR1kuGS+rTSa4LkaUd4Zl3pZ2M+PYR4J/chnBkVl70fRQBbCBiOi1/QtVniY+hOFR/x/r/sUYoTTVql2uy/mAsk12DXz5jwzFOsLEXCuagJxk9cCmzU8VTFLkIespup0A3HXFkdIihhUoXI24itIPmknn8umeJcgdSZkAc0uUzn/PFeg2Oul7any6DoLVA5nqpisp04w0NVSCxGEdNpS5fNKxpjm1HJr3xzqyySm21o2W8gokThV1y+NZsxGyRekjeDN5e5LeK2gTkLXyhtpFbEH6nGYYxHGYZrpt1ynamK41j8xp/FkibkGqzdBbkVuaLL+FcGy0PO6fGH2GyJEgPdOrAk3Jby1zaAz9UixLTwX31vCXeYVVStCwuHjT6uWKLDFNjXAUDRepg+TvejGUWKAuVF7QvH7hXoy2yuQT7abf7Z07TE0ZBTte+7UMUp/4rd4V6pWv/TiryLpkV3/8gUgNghfX5kP4jVxmXB0SHwdyeJ8rOjRt6KNgkK+SBds8GvB4ndj3QI7V9MXSH127yfNgwGcI74tekWIWjV/Z9mZZroZgbWbirINHV/2R4jvNihoEJOUQyqR1GC+x39Ew8jfjb1WgtVGJcZ4U=",  # noqa: E501
                "name": "Schnorr Proof",
                "public_key": "7+o8hAuyqbgCBixFFyIxUim4sGgjsVhQVP0o10ohgBN5++f2ohuBvSbBb9VzKx4vmRzd7sfCxwpAeo+z/QQVmDHWLrcp17y/kYbipB3cE3ewsneojyh+qEqY5H9/QiRZkC2X3XVqPVxJv5aVS3Um4vFsfCgS6uWc6HxayWu0TOgQu5FNH4hQxQH7QI68u4uthuvyUfH0t7rqXgOoBbXpm3vPrJBnLvCaxL3FBUvQH27nW5prQoRFCjzUZgEJJtUbykIPWCI/VMT/Ui8jwx3EA8bsVwUti3Mdptlv9MilOlPKo7ChaNg/vzVqsmX2xKXGXhBijgG1iey+5FnIZPQBs/fCkHc9h13pVaEJemJDhZIhiYQ2KxDmf2bWk/ZR5LKX4kFpyY+MI3KSkK2HGrvFiLej2Wxc3jWUK3LmVBCxxB1JrAX94k5fOalVGA74cNte1dp644fR+7h/7K4huDfoVbqh+arkMfg1VDEnPCMjPuox+mwR0DfDvL1niOFNwSNuSdeFqRMdj0Fcx5vG4KXCZTDlPUQIcu9VwdQnXJWqf1izh7Ol2Oi4//Y+3PX8BzMUSyt3L1x2h8kC7sHvIVO+bA9zEjN105X0RJcLkP6WM/27MyrlcfSbWAD2LOBoXySTxiv0wBuDxowo/X2nW7nTcHqu2gaabeZQGMf8/F9VI/o=",  # noqa: E501
                "response": "AQy+BIv++6QaVlDQNIpd45ZIarh/0weEaGTs8a4yJE8=",
                "usage": "SecretValue"
            }
        }, {
            "owner_id": "clara",
            "sequence_order": 2,
            "auxiliary_public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAxxobWJQjHoxb0//JfPa7\nvHkvoN7a+42OBJIPsQPeJKt9nT1yO7fZLnG2y3Ky+XMIYgzQIOArmcKwBqr/SKfY\nW9wAVDjf85Wiky5qK+jArKOzxnlzIvQKVLyouAXiBglN7NBALlVYPmGKQXRrl8eT\nYHv/F+99wLY2rmAcjGKgex091giV1GK/nYJ4+PawrA+sq0nkEPllc3ZQpAbR7/qc\nINweUpU/3eNNzL1tlIARXY/SVrviNVcpOmo4EdOiwRNvXQyNXOoy7UvWrEtrlyYS\nmSN2kH/6+TC21BUn49QFXT27iWITYWrMfWszUrr24V1Q/FLJCUX6IyAjDc7fiVhP\n2qhIGqG6z97nlQX8vBDW/CFXJjZ8SeZa+p2JmoUaTsOC72kMKAZ9jmYOZmbhnXYp\nrddlctbgdaCkdcRD2tzAQQs5q+H3Rn9iOlk0TAry3p1NkmDx6oVlqW38rHkpS5cx\nyxOuwNzY8wdTUWElGWaYqAfyoDEeFpDae9qH9N82s6DpXIG5eWU+ErufCNhaLRw+\nGnDkKdQ68jQI7+kuP01kWmIargRSgyPemWJ8hMrpU9mXx8fWej81+qb0C/Q3xGWO\nPBGJ/WYs9P3uC0a2cWDzcwMAtLsbeOO7AVjz0LhWMECS0Eqm6/YdF3raq4ypix4E\nNEATk52lfROv+Ojnn45u5JcCAwEAAQ==\n-----END PUBLIC KEY-----\n",  # noqa: E501
            "election_public_key": "b5B8KfI6Np2k4bLj5RPUGQHxdiwIo4mvPyd/tQCS1PFUrVQ/7oTZRP2tsWg50qAqIdGIjehholjWUgz6LRqSZiMRaWOaD6+GPvqVOA7W0hCBEKxca3M3qbCiRY5jCPIy1/s9cZgZtfATpNIKXpKCr9ekonPMFTbuJiiAOSZFwEIeFAi3xtVBon/NOgmRyqXPu7fUGzWNQlJAmOWMU7Xa9G/K3xlytgcvbicukuyv4aBONYzd2SNEQsO81mKDcI6fXnLbG/44pcbS6F2p2PATfMPLxTQV7cLN8+gG3FXsVt+J8+7Ou74iwoNK0/E/FtGhwqQxiLjsYasTRcXGcQfOBEvP5GpcHn+uGId9sZdCge/HPVQ1CNKA3XUOZSmEfyJirVew7PaTy9ux4YMWNliGTYGFDsIrQDilkEvUNH8P7B+9aTG2S24+gz5IuMGDZ9yEwXx4a1krk15XPsxMFmC0Asv95oueeDP6KZ2zln+9rqPhyDR9LXNYF82cGSi57oWgxdX/J7luwFrLlTbvKHneCxGaERNQZAq8KeuflqQFUrTbr6uNlRI7RfBYGkUbDkYuoX9v/kXH7FtwZMP+CVu9ntCjAQz0YT5SGQX4Qa8jSX89N1FP+caqX4ndqHw58bp0Fa6oG+GX3hlUBJeBQpYhIr8e4kWaxkzqt4P4wacYlSY=",  # noqa: E501
            "election_public_key_proof": {
                "challenge": "MK6CmlcHRCeI2Fq5GZAsonlUiD6VPcZHpXzM8gFWSoU=",
                "commitment": "XRoO9PiizLZ2q7UiA2887LSbAuIE/NRLpNibEh6G3BZSJfkTpIGhmOm/1Qiw2wbWqM8ndlPh64GV+D5wjzmUEchva6mwtvVNfDCsP+hm+ELAKDUH9O+tiIbpDn+uzb2Y/O4En+eh6XtFyAjh6a6kDKkuEtxVQ6KLmbDuNjc5c0Bz6vM+97uFqLoIV9nDhDAypCXOsBsrRQhkBcQ+1n1U35astAUpSM3gdRNzQdHvjO1Gh+G9eprr3uWYaMMv8m/sp4xTrLB6vno/Tbcwa1vdkzo7EeIu+xQQYuttqPgvFVhxErEaw7CHMgqVN5LBWcmI5nulvEEWYtS6m6eZ1oqB7BnLTOADIlR1f1UIL2xiCOwKqWGXhD2j4Y/XTujzE0ZGxTp8/jXLmLiH3QgW31q61KPkvPHgCLwZ5Ty9vGmRwe18hAZwPqpYaZAmcMSZX7F43pHC2UNJTp5Kr2YeHxaEi6N3cKSg1zFsL9CWBD7dGbfIAMxUsE/yKH805x/+HWm5tGf2sdxaeOvBhL29gC2g1WJdw2hNiWKDzAjjk6KlLQEgA9UgT3/93WcN5bTTrO8ETYIMAg7U8Pd1Rp6GR7wgKCox5aDZsXkOitvNMOHXWosMWl602oRGXMYN6iFUyWPdkMxpaYx2kFXx0Kc9UDH2D3stlvI0fSNykEdxBpyEdVs=",  # noqa: E501
                "name": "Schnorr Proof",
                "public_key": "b5B8KfI6Np2k4bLj5RPUGQHxdiwIo4mvPyd/tQCS1PFUrVQ/7oTZRP2tsWg50qAqIdGIjehholjWUgz6LRqSZiMRaWOaD6+GPvqVOA7W0hCBEKxca3M3qbCiRY5jCPIy1/s9cZgZtfATpNIKXpKCr9ekonPMFTbuJiiAOSZFwEIeFAi3xtVBon/NOgmRyqXPu7fUGzWNQlJAmOWMU7Xa9G/K3xlytgcvbicukuyv4aBONYzd2SNEQsO81mKDcI6fXnLbG/44pcbS6F2p2PATfMPLxTQV7cLN8+gG3FXsVt+J8+7Ou74iwoNK0/E/FtGhwqQxiLjsYasTRcXGcQfOBEvP5GpcHn+uGId9sZdCge/HPVQ1CNKA3XUOZSmEfyJirVew7PaTy9ux4YMWNliGTYGFDsIrQDilkEvUNH8P7B+9aTG2S24+gz5IuMGDZ9yEwXx4a1krk15XPsxMFmC0Asv95oueeDP6KZ2zln+9rqPhyDR9LXNYF82cGSi57oWgxdX/J7luwFrLlTbvKHneCxGaERNQZAq8KeuflqQFUrTbr6uNlRI7RfBYGkUbDkYuoX9v/kXH7FtwZMP+CVu9ntCjAQz0YT5SGQX4Qa8jSX89N1FP+caqX4ndqHw58bp0Fa6oG+GX3hlUBJeBQpYhIr8e4kWaxkzqt4P4wacYlSY=",  # noqa: E501
                "response": "+rqEwVYM7oQoPJtI/kuIwnoWRqUoyRANbgv58j5vwc0=",
                "usage": "SecretValue"
            }
        }
    ]


def trustees_partial_public_keys():
    return [
        {
            'owner_id': 'alicia',
            'designated_id': 'bob',
            'designated_sequence_order': 1,
            'encrypted_value': "\x9c¶þì\x915åþ8üô\x06¶\x13WF(D\x04ã¹\x12D7°'¯\t=¿ü\x18§$Ç\xa0WÃÆA\x0f3Âv\x00Æð\x8d\x026\x86*Z¬à\\ÿ(\x9b\x96\x16[(äÀt³úMòµ\x1fNH\x9c\x166K2é4\x03WºlÉÉ\x03\x88%-_d/S\x96ê;³\t\x99\x9e\x93^,Û\x89\x94ò³v´\\Ê3\x84Ê¾·¨\x18ÙÉ\x91ë\x80rD;>í<áð\x9e\x02©Y´üºe\x96ä!êïð\x06.Sq\x8bÇiv¹á>%ç'\x931×øÑÂ\x9d\x01ø\x88ùØ0Ùq\x9dó-\xa0l\x83\x84IÅ½ÿúy£Hkm(E¸æ®¸´XaýË\x9cF³T¾\x02¦Ì?â[ï\x9eÈÆ\x85A\r\x92¡bÍ\x01HÒ!ånEÕûBñ%HÝ|¬\x1bBÊÇ<°¨\x83ø\x1e:»\x0f]SÍD\x82HøÉè¥^x»gfú\x0c×\x1e©}\x01©Öæ=\x1e\x10R\x96\x82ôo\x800ÛG\x1dë³\x8f\x11ovtó²§AÖÜèmÛZ\x1eIÏ@\x11åd\x1fQNóüøO\x12,Kús\x06«Ö\x941;Þ5-\xa0\x94áñwÛ¹*¶\x16Et\x13yÖVÅ\x98\x87Óæe\n\x9düÊ®b\x99éÀ§\x8a¬)\x87«L?Q6\x16GHâñúr.\x081£Í6\x1cb\xadè2|\x9e}º\\\x8a\x8eMZ'_ë¬|\x88kÏ »áT]ròV?è~\x1aÖrEÃ\x82Ø\x87¶\x9a7P\x0c\x10\\[¡k]æ:\x06¿ßtDÐp8CÊ\x91\x02QN\x9c£\x07\x01\x80T:\x06\x99Áî\x89Ãñ7%½Ñ\x9có¡£\x86\x98o%\x19}O®~\x11|\x04Ë\n\x03¶ì°z\rFÃ(~8Á.\rÕ",  # noqa: E501
            'coefficient_commitments': [
                't+lrjkGIpnmdPpDq/pk2qwbi5y5qlM5U/60KKE11yISTX2nUdB3IpQdEKTfhg89GvJevTlbi0XS9wNSbAvCi/hyzVnoHXFWJy4E1GKYZRxbwzg+nZhr9AABa0eRPIXpjpB/z6ZTnlIs4MfxeHnIhoooJkEFfUry1N4EPXAZeh9lEAuiCOc/5fa8XmSILEzCef9TioBZK+OfG08Wn5Ft+Fr9zW7QQYzTess9rFLeYoY4V8lCNwBRUaPOEvy102gGPN3VbClxEcwAlKdeYEILYTVOWHfwfQ+UPbY5wVk3wfKdo5aHoB9/mBFcSpd+xbq60RW7/SxC1usirgrHfGwpKMDtUVgfP6kz5aW5H1YaKc0Cfv5nsLsEfnssTN7R1nDdJxrBjTqq/+nLo+F13Ak1du/XC8xmDgiVB/rAvFczAa+9HZ8Ou9rVL6HVUx9v+4lk12rKi1uToA3BipsWhfylcUru8A2geeg+kYSlLCFrg0FQs9IxxFi9otJVPd11vGf/I7WwgNohjBiQ2RrFy54/LyzA/ZraraeUmngpvG/65odg6n6LTA+p9F+LR+zyEY5vtAye5ps5lbFtlNMkEFhb8xFx52OITdWpYX5lQFr/SHyyS5eBeCDsBjQFPLfLI/XuubptFXSw5ZzVIw7rDbG5NsmJ+DcQcTUDstidLSerks2c=',  # noqa: E501
                '1InA2DR8F0dqjnxJeCIDs/dbogkQdWwmB161NZbLcYFdwKB9D5Ff50aAnBiq5BNuNBf1f+atlDwVff9mXDxtXGQDvbPXumyJ9ApnFZu9EaNIgVUwCVOttNbB7ABM3wyw1KYjX2Ao3H0fZ2ZJUpwi4mQ5Q35R7sCtkgYS8tAW4+eSsfxHdPl3FsIMPD+Ragaj8JsBdRrajLsAFlH2sPGvlKvvcqbFvRX4cs+5DF020e09nk37lQh0vdQ8zvrnwU6nWNGqHpkEiet9y8djdaepTgh9EoF+3odW6vu4Dd0VjzBTf6FBeJcmtPRSwy94sgNJXTxwEEkj1J/ueHFXsUQ73gx2bWSl68bhVfbrYUKVUmfWIbPembRmjZgLaLABh8fsa6+M7h/ACy7FcKyCx4XY+IgV59s4JueDfv2nowaWy8Ocn0EeQrE0MUFhL3kdOVX20SyahSxgWGa6iDjnuQJHimjpDdd/9SuNzoYMWTLAfFCpBkUf7IGDLHFpcfWDDl5iXeP2Vk+Q3weyI01VWF8mxllwyp3G45izzhbB0DMOdNDGBz30kQzZ6PCLHugKHqB20J/JrIPmIpJ0N8ATYNTlOysZtzkzDerJ1TXRWc4q0+RapLc/6HS+Vyf4WMjZ8Idnbtoz4mouewqOYX3hJ4zRsLPkAzHYfVqIM12FNA76JfM='  # noqa: E501
            ], 'coefficient_proofs': [
                {
                    'challenge': 'EvWzlYcCqbnqC8bWoNDLGIHCytF1O9DJG9xKeBB3hDQ=',
                    'commitment': 'HkTkHOzrm32eZea2M3rlNzbce91flDdW/a3kYcBLeB+nlBTvTIC9WSU6Xcz2YnBWH4BypFKIrvf+/C0dK6nc5YwoXPePxYtlJYeK671tXKkswpnirVtBi9XwzhOtO9ZFfOV7p1BTT1zQk0DtyrtiIUY3W7DmUI7h5p1gNubGMr3DeRXBQHlD0rQxWgKQIPeYX7EDZD1IGXouKF3TYK10yF25BE1nXPoJD7VhH9KeHAwE/OnFw6GPuTVgZD1TxI99o0Fo/rm7U7D5Eii9LjUB+lQmw1hPUd+7QhY2uf+i7Z8RZrgvAXvbxq256g2vV5DXRScnO2ZwYoK+ry+374FXfqEWBWbUC9uIlXxrZ6+8oPz6YYiMkQIPAvvXciIVoMTMSraOAibyPI/4tLLx+0/RklJYjxV04uM2KjTql21q6ReVUsEKDvUTzsEtMzYtxQpMEXjQEtdQeB86j9CdFYAFVGevre1o14mRuIVvWWQF9ZO3jsuyqFdX9PzumoZ8dc5lPkodv3olDHSITepnEMU1KWBMlgBEj7gqERi2Dywewg8DRY9bLEibH9HoxK2VoF7kEUw16mfFwZNO1yTHjOFPFrnLh9qVWTY+rRo0DO4oZQCbeCATYtyteKCdha8EiW/WiNMEyx9g978J9Ug3rfsitGZYJQSWqWrGHY65Ee93fM4=',  # noqa: E501
                    'name': 'Schnorr Proof',
                    'public_key': 't+lrjkGIpnmdPpDq/pk2qwbi5y5qlM5U/60KKE11yISTX2nUdB3IpQdEKTfhg89GvJevTlbi0XS9wNSbAvCi/hyzVnoHXFWJy4E1GKYZRxbwzg+nZhr9AABa0eRPIXpjpB/z6ZTnlIs4MfxeHnIhoooJkEFfUry1N4EPXAZeh9lEAuiCOc/5fa8XmSILEzCef9TioBZK+OfG08Wn5Ft+Fr9zW7QQYzTess9rFLeYoY4V8lCNwBRUaPOEvy102gGPN3VbClxEcwAlKdeYEILYTVOWHfwfQ+UPbY5wVk3wfKdo5aHoB9/mBFcSpd+xbq60RW7/SxC1usirgrHfGwpKMDtUVgfP6kz5aW5H1YaKc0Cfv5nsLsEfnssTN7R1nDdJxrBjTqq/+nLo+F13Ak1du/XC8xmDgiVB/rAvFczAa+9HZ8Ou9rVL6HVUx9v+4lk12rKi1uToA3BipsWhfylcUru8A2geeg+kYSlLCFrg0FQs9IxxFi9otJVPd11vGf/I7WwgNohjBiQ2RrFy54/LyzA/ZraraeUmngpvG/65odg6n6LTA+p9F+LR+zyEY5vtAye5ps5lbFtlNMkEFhb8xFx52OITdWpYX5lQFr/SHyyS5eBeCDsBjQFPLfLI/XuubptFXSw5ZzVIw7rDbG5NsmJ+DcQcTUDstidLSerks2c=',  # noqa: E501
                    'response': 'oTxU4o64GfIF8i21nKn8Yq6BXFhb9pWGWUxXm3fZL88=',
                    'usage': 'SecretValue'
                }, {
                    'challenge': 'VZjO9f767l3U1KmdZtnCrwCl03+/IS1Jbg+st3bET0I=',
                    'commitment': 'xenjsRW7v1VDRR6aUaSB+7VYVSEuw7Y7Rl1N1d8kMXPEOq8esSSlCserKljg3lpTbNKu+MyUxHl5RfczHusW7yCB+jm1ZWqC0atBD5KQ3mh2spOQ81+do2JSU9XzvbUqVgCeMHD/dbFRDV4tOGbwyRoTftTD9W2FcwZ8TL3mQujDQyu2LbDitLpG+UPJZiivf+rdgB/dyaBQyS2/Cnk21BOiAEKmVbok1I0ZNk1aYRDAiBysp+ctN3xdFTyfveslYGFgVqhD2+3vqM6CEY1+gM9vtEMFZuuFUb5vOP7Xg5rWwVI9bj4F8iIbwRX++RZiNT8isCpdTciVoMj2AX08RYs9WrxiymcTUtW5Bioleznhgdj2iu0ZmkBDd/r3O24Af87ncJe4wWRN2rKV13TyVSEOeHs5RZ+IgVuBlfeVaMY66bWJ3opHtfVmzZo4BSdyHkoDNZj3MTEO9xf9ZExv5IxOKaQ91mdNAlkrxjp5PkMlkuH3xWLIiTHqieazpG2ZjqVKGqe8waUcCVNcOL/F/b/Hz/kNsi5QHhEt1rtSpSkInxo3vIzm1gDpLnLI8RqlfWjkr6ad6DrAAHCI1jEPeoSF0BnTWcLklwC1Gf0vk6C7SWGPqYyF0/XUI+D8wMDYp/Xnq4GfjLy3Tb5gtp/F59AcuC72gkQnu48YOY6BtFk=',  # noqa: E501
                    'name': 'Schnorr Proof',
                    'public_key': '1InA2DR8F0dqjnxJeCIDs/dbogkQdWwmB161NZbLcYFdwKB9D5Ff50aAnBiq5BNuNBf1f+atlDwVff9mXDxtXGQDvbPXumyJ9ApnFZu9EaNIgVUwCVOttNbB7ABM3wyw1KYjX2Ao3H0fZ2ZJUpwi4mQ5Q35R7sCtkgYS8tAW4+eSsfxHdPl3FsIMPD+Ragaj8JsBdRrajLsAFlH2sPGvlKvvcqbFvRX4cs+5DF020e09nk37lQh0vdQ8zvrnwU6nWNGqHpkEiet9y8djdaepTgh9EoF+3odW6vu4Dd0VjzBTf6FBeJcmtPRSwy94sgNJXTxwEEkj1J/ueHFXsUQ73gx2bWSl68bhVfbrYUKVUmfWIbPembRmjZgLaLABh8fsa6+M7h/ACy7FcKyCx4XY+IgV59s4JueDfv2nowaWy8Ocn0EeQrE0MUFhL3kdOVX20SyahSxgWGa6iDjnuQJHimjpDdd/9SuNzoYMWTLAfFCpBkUf7IGDLHFpcfWDDl5iXeP2Vk+Q3weyI01VWF8mxllwyp3G45izzhbB0DMOdNDGBz30kQzZ6PCLHugKHqB20J/JrIPmIpJ0N8ATYNTlOysZtzkzDerJ1TXRWc4q0+RapLc/6HS+Vyf4WMjZ8Idnbtoz4mouewqOYX3hJ4zRsLPkAzHYfVqIM12FNA76JfM=',  # noqa: E501
                    'response': 'l96t7PzZBMLV7HM1Nvt00zOVa6mz4+sNwZbgbQErlFA=',
                    'usage': 'SecretValue'
                }
            ]
        }, {
            'owner_id': 'alicia',
            'designated_id': 'clara',
            'designated_sequence_order': 2,
            'encrypted_value': '8^\x08µJè¹j\x0fÑ~ä?ï\x06ÂW\x88\x95^N2I¢$yc½U§\x9d²ú\x9eè%3Ð"l\x85\x8f\x14©~³³3°\x83&ç·\x8f\x8b#úKç\x89¬\x80¯I[Z+Þ×ãª\x93\x97ØsJÖçp|\x91>ðOM\x19Õ¤Ø7\x8eï\x9e¹\x0e-¸\x12á³\x87è\x0f\x82á,·\x8fYAÎÎH\x9d\x8aHim.G¿#rß\x98kc\x05Eíx°zK\x8bA?ãÀ\x99ØÜ¦\x88\x19\xadä~ú\x9c\x0b¹3X\xad!LÑ²\x96?\x92Øâ\x8b«øùå\x19ªP\x12Äkï\x94ø8.ê0K\x1e\x99<_\x8e¸ÉX%\x0b\x9a¹Âí¤ÑñB\x06ý\x9b\x02-\x10S\x07\x81\x11ÑÈ\x06\x14f»µÈ%\x97K\x8f{h\x9b\x02\x0fãAø´1=Bâ¬^W\x80µ\x98õ´\x19zÜ¥\x97\n)B\x886°ög\x90\x88ù\x1c$¹\x19\x07"Ò´\x18Ø\x7f\x94DÄ)>5\x00:ü§¾÷3\t9\tcéEÔÂ\xad\x91#\x91«Ä\x9bS-N\xadç\x02½E\x9fÉ/µÃ\x9c}bþ9\x1fç\x19¢Ij\x11ÿ\x0f»àQÔ[à²£"³\x0cA£å§·x}Ü\xa0ó\x97áu?vÛÄÜSI6\x10÷wð \x10à&\x13\nÔ,îc\x0b?¨b#Ù\x19$\x8f«,qþzhÑ\x0c\x18f§ô¦1x¹\x95|À\x95ð$\x85DÜA\x0b\x86\x1cÞ\x0c\x8d\x07\x10$£\x99J\x1aÃ\x95âTZÌÐdÚ\x8aKa\x1eO\x8c\xa0\x8bH\x97ø²_£«Ð%?·Âf\x93GuÑ\xad9Å\x02ð$ZP\x1e·üóÝí9à¸%óSÜ½U½¢³Q¥\xad\xa0\x1dío[¬\x92\x19Øzf,!Ó¬ÙÑ\x12F}\\?H\x83³/\x0bP[',  # noqa: E501
            'coefficient_commitments': [
                't+lrjkGIpnmdPpDq/pk2qwbi5y5qlM5U/60KKE11yISTX2nUdB3IpQdEKTfhg89GvJevTlbi0XS9wNSbAvCi/hyzVnoHXFWJy4E1GKYZRxbwzg+nZhr9AABa0eRPIXpjpB/z6ZTnlIs4MfxeHnIhoooJkEFfUry1N4EPXAZeh9lEAuiCOc/5fa8XmSILEzCef9TioBZK+OfG08Wn5Ft+Fr9zW7QQYzTess9rFLeYoY4V8lCNwBRUaPOEvy102gGPN3VbClxEcwAlKdeYEILYTVOWHfwfQ+UPbY5wVk3wfKdo5aHoB9/mBFcSpd+xbq60RW7/SxC1usirgrHfGwpKMDtUVgfP6kz5aW5H1YaKc0Cfv5nsLsEfnssTN7R1nDdJxrBjTqq/+nLo+F13Ak1du/XC8xmDgiVB/rAvFczAa+9HZ8Ou9rVL6HVUx9v+4lk12rKi1uToA3BipsWhfylcUru8A2geeg+kYSlLCFrg0FQs9IxxFi9otJVPd11vGf/I7WwgNohjBiQ2RrFy54/LyzA/ZraraeUmngpvG/65odg6n6LTA+p9F+LR+zyEY5vtAye5ps5lbFtlNMkEFhb8xFx52OITdWpYX5lQFr/SHyyS5eBeCDsBjQFPLfLI/XuubptFXSw5ZzVIw7rDbG5NsmJ+DcQcTUDstidLSerks2c=',  # noqa: E501
                '1InA2DR8F0dqjnxJeCIDs/dbogkQdWwmB161NZbLcYFdwKB9D5Ff50aAnBiq5BNuNBf1f+atlDwVff9mXDxtXGQDvbPXumyJ9ApnFZu9EaNIgVUwCVOttNbB7ABM3wyw1KYjX2Ao3H0fZ2ZJUpwi4mQ5Q35R7sCtkgYS8tAW4+eSsfxHdPl3FsIMPD+Ragaj8JsBdRrajLsAFlH2sPGvlKvvcqbFvRX4cs+5DF020e09nk37lQh0vdQ8zvrnwU6nWNGqHpkEiet9y8djdaepTgh9EoF+3odW6vu4Dd0VjzBTf6FBeJcmtPRSwy94sgNJXTxwEEkj1J/ueHFXsUQ73gx2bWSl68bhVfbrYUKVUmfWIbPembRmjZgLaLABh8fsa6+M7h/ACy7FcKyCx4XY+IgV59s4JueDfv2nowaWy8Ocn0EeQrE0MUFhL3kdOVX20SyahSxgWGa6iDjnuQJHimjpDdd/9SuNzoYMWTLAfFCpBkUf7IGDLHFpcfWDDl5iXeP2Vk+Q3weyI01VWF8mxllwyp3G45izzhbB0DMOdNDGBz30kQzZ6PCLHugKHqB20J/JrIPmIpJ0N8ATYNTlOysZtzkzDerJ1TXRWc4q0+RapLc/6HS+Vyf4WMjZ8Idnbtoz4mouewqOYX3hJ4zRsLPkAzHYfVqIM12FNA76JfM='   # noqa: E501
            ],
            'coefficient_proofs': [
                {
                    'challenge': 'EvWzlYcCqbnqC8bWoNDLGIHCytF1O9DJG9xKeBB3hDQ=', 'commitment': 'HkTkHOzrm32eZea2M3rlNzbce91flDdW/a3kYcBLeB+nlBTvTIC9WSU6Xcz2YnBWH4BypFKIrvf+/C0dK6nc5YwoXPePxYtlJYeK671tXKkswpnirVtBi9XwzhOtO9ZFfOV7p1BTT1zQk0DtyrtiIUY3W7DmUI7h5p1gNubGMr3DeRXBQHlD0rQxWgKQIPeYX7EDZD1IGXouKF3TYK10yF25BE1nXPoJD7VhH9KeHAwE/OnFw6GPuTVgZD1TxI99o0Fo/rm7U7D5Eii9LjUB+lQmw1hPUd+7QhY2uf+i7Z8RZrgvAXvbxq256g2vV5DXRScnO2ZwYoK+ry+374FXfqEWBWbUC9uIlXxrZ6+8oPz6YYiMkQIPAvvXciIVoMTMSraOAibyPI/4tLLx+0/RklJYjxV04uM2KjTql21q6ReVUsEKDvUTzsEtMzYtxQpMEXjQEtdQeB86j9CdFYAFVGevre1o14mRuIVvWWQF9ZO3jsuyqFdX9PzumoZ8dc5lPkodv3olDHSITepnEMU1KWBMlgBEj7gqERi2Dywewg8DRY9bLEibH9HoxK2VoF7kEUw16mfFwZNO1yTHjOFPFrnLh9qVWTY+rRo0DO4oZQCbeCATYtyteKCdha8EiW/WiNMEyx9g978J9Ug3rfsitGZYJQSWqWrGHY65Ee93fM4=', 'name': 'Schnorr Proof', 'public_key': 't+lrjkGIpnmdPpDq/pk2qwbi5y5qlM5U/60KKE11yISTX2nUdB3IpQdEKTfhg89GvJevTlbi0XS9wNSbAvCi/hyzVnoHXFWJy4E1GKYZRxbwzg+nZhr9AABa0eRPIXpjpB/z6ZTnlIs4MfxeHnIhoooJkEFfUry1N4EPXAZeh9lEAuiCOc/5fa8XmSILEzCef9TioBZK+OfG08Wn5Ft+Fr9zW7QQYzTess9rFLeYoY4V8lCNwBRUaPOEvy102gGPN3VbClxEcwAlKdeYEILYTVOWHfwfQ+UPbY5wVk3wfKdo5aHoB9/mBFcSpd+xbq60RW7/SxC1usirgrHfGwpKMDtUVgfP6kz5aW5H1YaKc0Cfv5nsLsEfnssTN7R1nDdJxrBjTqq/+nLo+F13Ak1du/XC8xmDgiVB/rAvFczAa+9HZ8Ou9rVL6HVUx9v+4lk12rKi1uToA3BipsWhfylcUru8A2geeg+kYSlLCFrg0FQs9IxxFi9otJVPd11vGf/I7WwgNohjBiQ2RrFy54/LyzA/ZraraeUmngpvG/65odg6n6LTA+p9F+LR+zyEY5vtAye5ps5lbFtlNMkEFhb8xFx52OITdWpYX5lQFr/SHyyS5eBeCDsBjQFPLfLI/XuubptFXSw5ZzVIw7rDbG5NsmJ+DcQcTUDstidLSerks2c=', 'response': 'oTxU4o64GfIF8i21nKn8Yq6BXFhb9pWGWUxXm3fZL88=', 'usage': 'SecretValue'}, {'challenge': 'VZjO9f767l3U1KmdZtnCrwCl03+/IS1Jbg+st3bET0I=', 'commitment': 'xenjsRW7v1VDRR6aUaSB+7VYVSEuw7Y7Rl1N1d8kMXPEOq8esSSlCserKljg3lpTbNKu+MyUxHl5RfczHusW7yCB+jm1ZWqC0atBD5KQ3mh2spOQ81+do2JSU9XzvbUqVgCeMHD/dbFRDV4tOGbwyRoTftTD9W2FcwZ8TL3mQujDQyu2LbDitLpG+UPJZiivf+rdgB/dyaBQyS2/Cnk21BOiAEKmVbok1I0ZNk1aYRDAiBysp+ctN3xdFTyfveslYGFgVqhD2+3vqM6CEY1+gM9vtEMFZuuFUb5vOP7Xg5rWwVI9bj4F8iIbwRX++RZiNT8isCpdTciVoMj2AX08RYs9WrxiymcTUtW5Bioleznhgdj2iu0ZmkBDd/r3O24Af87ncJe4wWRN2rKV13TyVSEOeHs5RZ+IgVuBlfeVaMY66bWJ3opHtfVmzZo4BSdyHkoDNZj3MTEO9xf9ZExv5IxOKaQ91mdNAlkrxjp5PkMlkuH3xWLIiTHqieazpG2ZjqVKGqe8waUcCVNcOL/F/b/Hz/kNsi5QHhEt1rtSpSkInxo3vIzm1gDpLnLI8RqlfWjkr6ad6DrAAHCI1jEPeoSF0BnTWcLklwC1Gf0vk6C7SWGPqYyF0/XUI+D8wMDYp/Xnq4GfjLy3Tb5gtp/F59AcuC72gkQnu48YOY6BtFk=', 'name': 'Schnorr Proof', 'public_key': '1InA2DR8F0dqjnxJeCIDs/dbogkQdWwmB161NZbLcYFdwKB9D5Ff50aAnBiq5BNuNBf1f+atlDwVff9mXDxtXGQDvbPXumyJ9ApnFZu9EaNIgVUwCVOttNbB7ABM3wyw1KYjX2Ao3H0fZ2ZJUpwi4mQ5Q35R7sCtkgYS8tAW4+eSsfxHdPl3FsIMPD+Ragaj8JsBdRrajLsAFlH2sPGvlKvvcqbFvRX4cs+5DF020e09nk37lQh0vdQ8zvrnwU6nWNGqHpkEiet9y8djdaepTgh9EoF+3odW6vu4Dd0VjzBTf6FBeJcmtPRSwy94sgNJXTxwEEkj1J/ueHFXsUQ73gx2bWSl68bhVfbrYUKVUmfWIbPembRmjZgLaLABh8fsa6+M7h/ACy7FcKyCx4XY+IgV59s4JueDfv2nowaWy8Ocn0EeQrE0MUFhL3kdOVX20SyahSxgWGa6iDjnuQJHimjpDdd/9SuNzoYMWTLAfFCpBkUf7IGDLHFpcfWDDl5iXeP2Vk+Q3weyI01VWF8mxllwyp3G45izzhbB0DMOdNDGBz30kQzZ6PCLHugKHqB20J/JrIPmIpJ0N8ATYNTlOysZtzkzDerJ1TXRWc4q0+RapLc/6HS+Vyf4WMjZ8Idnbtoz4mouewqOYX3hJ4zRsLPkAzHYfVqIM12FNA76JfM=', 'response': 'l96t7PzZBMLV7HM1Nvt00zOVa6mz4+sNwZbgbQErlFA=', 'usage': 'SecretValue'}]}]   # noqa: E501


def joint_election_key_test_message():
    return {
        "joint_election_key": "0nOW5bz3DrLecByUXW2H/WsK87OyCSeUVJf8Y4Vn4q923ofId84xnfglP9Dbz7unATSCrfP6xpuJ3f8vk5occs4yvnv4HR83lqqP+/yyCajVqQLSgMTpUTi/lh5fA4qe7ndVbg5twOPNDgcHVCUTici6xh7hdPmVo92a6nP4AAmA8y1l8VqTF8WrWAPm1PeILHOTpj0xRhNhAeg/SYxIu61mmkJ2MNch/T0xDFk1YlcT4+WZzYkI+oGb41ZKtrmu5IpXBzbUf0YiRW/6MnqIK2VOf9sTRGLh+bK841KL9EPR4cNyoymP/kfvnoauHuHDuvclKClC0izGbUsovFG2cz/r6FjvelMt9eVc9ccNA0/grjM8whdkDYpQtaQynTHxMD3OCyqW2mcFEzFPWmhLP9kmRE43sBTCQtYdJ+lip+urpAw+y6+L1RraykGzg5NVhm2Pa8UV34522YB4lhsOU7b/Do9WdtvWxReY+HJOIMJwaROgybn0eV4v+E13q0WJDK31JA/o7IHIPGlRVbkcb6/0qrDbho0pCRgjQAtQ6i3JxRXpMDAEblWP5h38qJHQwpmIl9v9b1i5RVBge4LhxQXAAatvrZcPI4QZUmvtpXXJ7jP2KBGUbVmmsFKrmTO/7u76nydqmg3yFbDywfr9wg3PCLBUUx5WWil0TmVdeNE="  # noqa: E501
    }
