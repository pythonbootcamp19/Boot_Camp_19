from flask import Flask, request
import json
import weather_info

app = Flask(__name__)

@app.route('/')
def get_weather_data():
    city = request.args.get("city")
    if city == None:
        response = "Please enter a city in the url."
        return response
    else:
        weather_data = weather_info.main(city)
        weather_data_json = json.dumps(weather_data)
        return weather_data_json

@app.route('/all_data')

def get_weather_data():
    data = request.args.get("all_data")

    if all_data == True:
        weather_data = json.loads(json_data)
        # https://codebeautify.org/jsonviewer
        # json viewer
        important_data = {}

        important_keys = ["weather_state_name",
            "id",
            "weather_state_abbr",
            # "wind_direction_compass",
            # "created",
            # "applicable_date",
            # "min_temp",
            # "max_temp",
            # "the_temp",
            # "wind_speed",
            # "wind_direction",
            # "air_pressure",
            # "humidity",
            # "visibility",
            # "predictability",
            ]

    single_day_data = weather_data["consolidated_weather"][0]

    if all == False:
        for single_key in important_keys:
            important_data[single_key] = single_day_data[single_key]

        return important_data
    else:
        return single_day_data


#If you import this file/code to somewhere else it won't work.
if __name__ == "__main__":
    app.run(debug=True)