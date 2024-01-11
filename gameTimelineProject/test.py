from gameTimelineProject import GameTimelineGenerator

program = GameTimelineGenerator()

response = program.makeCall("NA1_4794682594")

print(response.text)