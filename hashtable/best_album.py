from collections import defaultdict

def solution(genres, plays):
    track_list = list((genre, play, i) for i, (genre, play) in enumerate(zip(genres, plays)))
    track_list = sorted(track_list, key=lambda x: x[1], reverse=True)

    track_dict = defaultdict(list)
    genre_sum_dict = defaultdict(int)
    for track in track_list:
        genre_sum_dict[track[0]] += track[1]
        if len(track_dict[track[0]]) < 2:
            track_dict[track[0]].append((track[1], track[2]))
        elif len(track_dict[track[0]]) == 2:
            if track_dict[track[0]][1][0] == track[1] and track_dict[track[0]][1][1] > track[2]:
                track_dict[track[0]] = (track[1], track[2])
                
    genre_sum_list = []
    for k, v in genre_sum_dict.items():
        genre_sum_list.append((k, v))
    genre_sum_list = sorted(genre_sum_list, key=lambda x: x[1], reverse=True)
    
    result = []
    for key, value in genre_sum_list:
        for track in track_dict[key]:
            result.append(track[1])
    return result

print(solution(genres=["classic", "pop", "classic", "classic", "pop"], plays=[500, 600, 150, 800, 2500]))