import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

arquivo = Path(__file__).parent / "air_quality_no2.csv"

air_quality = pd.read_csv(arquivo)

air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])
print(air_quality.head())

air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

print(air_quality_renamed.head())
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
print(air_quality_renamed.head())


#https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html

air_quality = air_quality.rename(columns={"date.utc": "datetime"})
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
print(air_quality["datetime"].min(), air_quality["datetime"].max())


#https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html
air_quality.plot(x="datetime", y=["station_paris", "station_antwerp", "station_london"])
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()