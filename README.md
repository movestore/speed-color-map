# Speed Colour Map

MoveApps

Github repository: *github.com/movestore/speed-color-map*

## Description
This is a simple Python Example App that generates a plot of the tracks coloured by speed.

## Documentation
Using the MovingPandas package, each location of all tracks is assinged a speed using the add_speed() function. The tracks are then plotted very simply, but each location is coloured by its estimated speed. This provides an idea where the animals were moving faster or slower. Line width can be selected and if a legend is to be added.

### Input data
TrajectoryCollection of the MovingPandas package

### Output data
TrajectoryCollection of the MovingPandas package

### Artefacts
`speed_map.png`: Simple map of tracks coloured by speed.

### Parameters 
**Line width (`line_width`)**: Defined width of track lines in plot. Default: 2.

**Include legend? (`legend`)**: Indicate if a legend shall be included in the plot. Default: false.

### Null or error handling
**Setting `line_width`**: must be a positive value. If too large or too small, the tracks might become difficult to see.

**Setting `legend`:** The legend makes the plot area smaller, but allows to discern which speeds the colours indicate.

**Data**: Input data are returned.

