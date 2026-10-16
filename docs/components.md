# Components and roles

This is a functional inventory, not a procurement-ready bill of materials. Quantities are omitted unless explicitly reported or clearly visible.

| Component | Role | Evidence / status |
| --- | --- | --- |
| Optical transmitter / laser modules | Convert electrical states into light | Laser use reported; rows of modules visible; exact type and count unverified |
| LDR receiver | Convert illumination into resistance change | Reported; exact sensor model and interface unverified |
| 7486 XOR gate ICs | Parity generation/checking and conditional bit inversion | Reported; package legends unreadable in photos |
| 7405 inverter ICs | Complement logic signals | Reported; open-collector outputs need pull-ups; exact circuit role unverified |
| Two 16:1 multiplexers | Select one of 16 signals or implement Boolean functions | Quantity/type reported; part numbers and wiring unverified |
| BCD-to-seven-segment decoder circuitry | Translate a decimal digit into display segment signals | Reported; driver model unverified |
| Seven-segment display modules | Visual numeric output | Three lit modules visible in the overall photograph; signal assignment unverified |
| Pushbuttons | User controls | Visible; direct data entry versus error injection unverified |
| Resistors, LEDs, DIP packages, wires and breadboards | Interface, indication, logic and interconnection | Visible; complete counts/ratings unverified |
| Power source and optical drivers | Supply and drive the hardware | Exact regulator, supply ratings and laser driver topology unverified |

## Digital logic notes

The 7486 family contains four independent two-input XOR gates. Cascaded XOR operations form parity; `b XOR 0 = b` and `b XOR 1 = NOT b` allow a correction flag to invert a selected bit. [1]

The 7405 is a six-channel inverter with open-collector outputs. Its output requires a pull-up arrangement to produce a valid HIGH. Pull-up sizing must match load, output current and timing needs; no resistor value is asserted for this prototype. [2]

A 16:1 multiplexer uses four select bits to choose one data input. It can also realize a four-variable Boolean function by setting its 16 data inputs to the function's truth table. Two devices alone do not establish the full correction architecture. If the actual device is a 74150, note its inverted output; 74150 is a reference example, not a photo-confirmed part. [3]

The display driver must match the common-anode/common-cathode display. The 7447A family, for example, has active-low outputs for common-anode displays. Its identity in this project is unconfirmed. BCD represents decimal 0-9; values 10-15 are not valid single-digit BCD. [4]

See [reference list](references.md).
