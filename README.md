# Raspberry-Pi-3-Weather

The purpose of this program is to query Open Weather (http://openweathermap.org/api) and dislay the data.

Coming from a PHP background, along the way I hope to achieve the following couple of things;

* Learn Python - for querying and interpreting data from the OpenWeatherMaps service.
* Learn PyQt4 - a set of C++ libraries and development tools that includes platform independent abstractions for desigining the graphical user interfaces.

This project is currently a WIP and does not yet contain a viable release candidate!

If need be, the config/weatherConfig.json currently looks like this;
~~~json
{
    "api_key": "your_api_key_from_open_weather_maps_org",
    "location": "2925533",
    "request_type": "weather",    // Allowed values; weather, forecast5, forecast16
    "forecast_count_5": 5,
    "forecast_count_16": 16,
    "units": "metric",            // Allowed values; metric, imperial
    "lang": "en"
}
