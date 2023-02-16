# State estimation in the National Interconnected System: an approach considering SCADA and PMU measurements

In this repository I am making available the codes developed for my undergraduate thesis entitled "State estimation in the National Interconnected System: an approach considering SCADA and PMU measurements" as a requirement to obtain a bachelorette degree as electrical engineer.

State Estimation code using pandapower library for power system analysis considering a 107-bus test system which represents the brazilian national electrical grid (SIN).

State Estimation is 
First of all we should 

## Power Flow

Consider a $K$ set of buses of a system. The active and reactive powers in a $k$ bus can be described by the equations below:

$$P_k = V_k \cdot \sum_{m \in K} V_m \cdot (G_{km} \cos{(\theta_{km})} + B_{km} \sin{(\theta_{km})})$$

$$Q_k = V_k \cdot \sum_{m \in K} V_m \cdot (G_{km} \sin{(\theta_{km})} - B_{km} \cos{(\theta_{km})})$$

The power flows through a transmission line between buses $k$ and $m$ and the magnitude of the current in that same line can be described using the beneath equation:

$$P_{km} = V_k^2 \cdot (G_{kk} + G_{km}) - V_k V_m \cdot (G_{km}\cos{(\theta_{km})} + B_{km}\sin{(\theta_{km})})$$

$$Q_{km} = -V_k^2 \cdot (B_{kk} + B_{km}) + V_k V_m \cdot (G_{km}\sin{(\theta_{km})} + B_{km}\cos{(\theta_{km})})$$

$$I_{km} = \frac{\sqrt{P_{km}^2 + Q_{km}^2}}{V_k}$$

In the above formulation, the terms $G_{km}$ and $B_{km}$ are, respectively, the conductance and susceptance of the transmission line, while the angular offset between two buses is given by the equation $\theta_{km} = \theta_{k} - \theta_{m}$.

## State Estimation


