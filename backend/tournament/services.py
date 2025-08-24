from tournament.models import Equipe


def update_equipes_points(
    equipe_1: Equipe,
    equipe_2: Equipe,
    score_equipe_1: int,
    score_equipe_2: int,
    match_deleted: bool = False,
):
    """
    Updates the points of two teams (equipes) based on the result of a match.

    Points are awarded as follows:
    - 3 points to the winning team
    - 1 point to each team in case of a draw
    - 0 points to the losing team

    After updating the points, the changes are saved to the database.

    Args:
        equipe_1 (Equipe): The first team participating in the match.
        equipe_2 (Equipe): The second team participating in the match.
        score_equipe_1 (int): The score achieved by the first team.
        score_equipe_2 (int): The score achieved by the second team.
    """
    # if the match is deleted we need to remove the points
    if match_deleted:

        equipe_1.buts_marques -= score_equipe_1
        equipe_2.buts_marques -= score_equipe_2

        equipe_1.buts_recus -= score_equipe_2
        equipe_2.buts_recus -= score_equipe_1

        if score_equipe_1 == score_equipe_2:
            equipe_1.points -= 1
            equipe_2.points -= 1
        elif score_equipe_1 > score_equipe_2:
            equipe_1.points -= 3
        else:
            equipe_2.points -= 3
        equipe_1.points = max(equipe_1.points, 0)
        equipe_2.points = max(equipe_2.points, 0)
    # else we need to add the points
    else:

        equipe_1.buts_marques += score_equipe_1
        equipe_2.buts_marques += score_equipe_2
        equipe_1.buts_recus += score_equipe_2
        equipe_2.buts_recus += score_equipe_1

        if score_equipe_1 == score_equipe_2:
            equipe_1.points += 1
            equipe_2.points += 1
        elif score_equipe_1 > score_equipe_2:
            equipe_1.points += 3
        else:
            equipe_2.points += 3

    equipe_1.save()
    equipe_2.save()
