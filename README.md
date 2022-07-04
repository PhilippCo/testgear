# testgear
Package to control a lot of testgear in an easy and uniform way

to install type: 

```
pip3 install git+https://github.com/PhilippCo/testgear.git#egg=testgear
```

## Multimeter
The multimeter configuration is done by using a method for every function to make use of autocompletion during writing your code.

### DCV measurement
```python
conf_function_DCV(mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1)
```
Configures the instrument to measure DC volts
* mrange: sets the range of function. If mrange is None (default) the meter is set to autorange
* nplc: sets the number of power line cycles to integrate one measurement
* AutoZero: swictches AutoZero for everymeasurement on and off
* HiZ: sets the meter to high impedance input (if possible)
* channel: selects the channel of meter, if more than one is availble

### ACV measurement
```python
conf_function_ACV(mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1)
```

### DCI measurement
```python
conf_function_DCI(mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1)
```

### ACI measurement
```python
conf_function_ACI(mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1)
```

### Ohm 2W measurement
```python
conf_function_OHM2W(mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1)
```
Configures the instrument to measure OHMs with 2 wires
* OffsetCompensation: enables the offset compensation feature of the meter

### Ohm 4W measurement
```python
conf_function_OHM4W(mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1)
```
Configures the instrument to measure OHMs with 4 wires




## Sources

```python
set_output(voltage=None, current=None, enabled=True, resistance=None, frequency=None, channel=1)
```


# supported instruments

## Multimeter, Electrometer

### HP, Agilent & Keysight
- HP 3458A
- HP 34401A
- HP 34970A (HP 34972A)
- Keysight 34461A (34460A should work as well)
- Keysight 34470A (34465A should work as well)

### Keithley
- Keithley 182
- Keithley 617

### Fluke
- Fluke 8508A
- Fluke 8588A

## Frequency Counter

### HP, Agilent & Keysight
- HP53131A (HP53132A works as well)

## Power Supplies

### HP, Agilent & Keysight
- Agilent 6632B
- HP 603xA

### Korad
- KA3005P

# Calibrator

### Fluke
- Fluke 5730A (57XX should work, but untested)
- Fluke 5450A
- Fluke 5440B

### Knick
- Knick JS3010

### Valhalla
- Valhalla 2703

# Multiplexer, Switches

### Cotech
- Cotech DIY Low Thermal Switch

### HP, Agilent & Keysight
- HP 3488A

# Function Generator

## Siglent
- Siglent SDG1025

# Scopes

# Temperature Controller/Meter

## Ahlborn
- Almemo 1030

## LakeShore
- LakeShore 331
