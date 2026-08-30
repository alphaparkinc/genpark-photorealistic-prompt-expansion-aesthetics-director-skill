from client import PhotorealisticPromptExpansionAestheticsDirectorClient

def main():
    client = PhotorealisticPromptExpansionAestheticsDirectorClient()
    res = client.expand_aesthetics_prompt('Futuristic orbital space station observation deck')
    print('Aesthetics Director: ' + res['director_session_id'] + ' (Sensor: ' + res['sensor_profile'] + ')')
    print('Lighting Score: ' + str(res['lighting_and_volumetrics_score_pct']) + '% | Realism Gain: +' + str(res['photorealism_index_gain_pct']) + '%')
    print('Expanded Prompt:\n' + res['expanded_cinematic_prompt'])

if __name__ == '__main__':
    main()
