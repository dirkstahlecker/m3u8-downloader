import re

text = '''Videos for download
https://damb2tknfsomm.cloudfront.net/uploaded/JQLqNkmwzaMN7BLP1DOoLjZPzblJ9Y4W/playlist.m3u8

RESOLUTION: 1280x720, URL: https://damb2tknfsomm.cloudfront.net/uploaded/JQLqNkmwzaMN7BLP1DOoLjZPzblJ9Y4W/1080p_5800k_v4.m3u8

RESOLUTION: 1280x720, URL: https://damb2tknfsomm.cloudfront.net/uploaded/JQLqNkmwzaMN7BLP1DOoLjZPzblJ9Y4W/720p_3000k_v4.m3u8

RESOLUTION: 854x480, URL: https://damb2tknfsomm.cloudfront.net/uploaded/JQLqNkmwzaMN7BLP1DOoLjZPzblJ9Y4W/480p_1600k_v4.m3u8

RESOLUTION: 640x360, URL: https://damb2tknfsomm.cloudfront.net/uploaded/JQLqNkmwzaMN7BLP1DOoLjZPzblJ9Y4W/360p_800k_v4.m3u8

RESOLUTION: 240x134, URL: https://damb2tknfsomm.cloudfront.net/uploaded/JQLqNkmwzaMN7BLP1DOoLjZPzblJ9Y4W/136p_400k_v4.m3u8

URL: https://damb2tknfsomm.cloudfront.net/uploaded/JQLqNkmwzaMN7BLP1DOoLjZPzblJ9Y4W/192k_audio_v4.m3u8

AUDIO

ID: audio-0, NAME: Default, URL: https://damb2tknfsomm.cloudfront.net/uploaded/JQLqNkmwzaMN7BLP1DOoLjZPzblJ9Y4W/192k_audio_v4.m3u8

Parts to download: 225
part 1
part 15
part 62
part 2
part 30
part 55
part 16
part 17
part 18
part 19
part 20
part 21
part 22
part 23
part 24
part 25
part 26
part 27
part 28
part 29
part 36
part 37
part 38
part 42
part 46
part 49
part 52
part 57
part 65
part 67
part 69
part 70
part 79
part 91
part 105
part 107
part 109
part 110
part 114
part 121
part 123
part 56
part 58
part 59
part 66
part 74
part 83
part 94
part 100
part 103
part 112
part 117
part 124
part 127
part 128
part 3
part 4
part 5
part 6
part 7
part 8
part 9
part 10
part 11
part 12
part 13
part 14
part 60
part 61
part 72
part 73
part 81
part 82
part 84
part 86
part 64
part 90
part 98
part 77
part 106
part 78
part 113
part 120
part 126
part 85
part 88
part 92
part 97
part 99
part 102
part 104
part 108
part 111
part 115
part 116
part 118
part 119
part 31
part 32
part 33
part 34
part 35
part 39
part 40
part 41
part 43
part 44
part 45
part 47
part 48
part 50
part 51
part 53
part 54
part 63
part 68
part 71
part 75
part 76
part 80
part 87
part 89
part 93
part 95
part 96
part 101
part 122
part 125
part 129
part 130
part 133
part 132
part 135
part 136
part 131
part 134
part 137
part 138
part 139
part 144
part 147
part 150
part 151
part 155
part 160
part 163
part 164
part 167
part 173
part 178
part 180
part 188
part 189
part 192
part 200
part 205
part 209
part 211
part 215
part 218
part 223
part 145
part 153
part 154
part 158
part 166
part 169
part 174
part 177
part 183
part 195
part 216
part 217
part 221
part 224
part 140
part 146
part 152
part 159
part 165
part 171
part 175
part 182
part 184
part 187
part 190
part 194
part 204
part 206
part 212
part 143
part 157
part 162
part 141
part 172
part 142
part 181
part 148
part 185
part 149
part 191
part 156
part 197
part 161
part 201
part 168
part 210
part 170
part 214
part 176
part 222
part 179
part 225
part 186
part 193
part 196
part 198
part 199
part 202
part 203
part 207
part 208
part 213
part 219
part 220
All parts downloaded.'''

def findVideoUrl(rawStr):
	m = re.search('RESOLUTION:\s*[\d|x]+,\s*URL:\s*([\S]+)', rawStr)
	videoURL = m.group(1)
	print(videoURL)

	# print (m.group(m.groups() - 1))

	# strForAudio = rawStr.substr(rawStr.indexOf(videoURL))

	# audioRe = re.compile( , re.S | re.M)
	audioMatches = re.findall('URL:\s*([\S]+)', rawStr)
	audioUrl = audioMatches[len(audioMatches) -1]
	print(audioUrl)



findVideoUrl(text)
