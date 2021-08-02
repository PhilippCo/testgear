# testgear
Package to control a lot of testgear in an easy and uniform way


## Multimeter
The multimeter configuration is done by using a method for every function to make use of autocompletion during writing your code.


```python
conf_function_DCV(mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1)
```
Configures the instrument to measure DC volts
* mrange: sets the range of function. If mrange is None (default) the meter is set to autorange
* nplc: sets the number of power line cycles to integrate one measurement
* AutoZero: swictches AutoZero for everymeasurement on and off
* HiZ: sets the meter to high impedance input (if possible)
* channel: selects the channel of meter, if more than one is availble


```python
conf_function_ACV(mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1)
```

```python
conf_function_DCI(mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1)
```

```python
conf_function_ACI(mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1)
```

```python
conf_function_OHM2W(mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1)
```
Configures the instrument to measure OHMs with 2 wires
* OffsetCompensation: enables the offset compensation feature of the meter

```python
conf_function_OHM4W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1)
```
Configures the instrument to measure OHMs with 4 wires




## Sources

```python
set_output(voltage=None, current=None, enabled=True, resistance=None, frequency=None, channel=1)
```
