[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
<!-- [![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.1-blue.svg)](https://doi.org/10.25663/brainlife.app.435) -->

# Description

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes edge time series (element-wise products of z-scored regional time series for every region pair) from regional fMRI time series.**

Z-scores each regional fMRI time series and multiplies every pair of regions frame by frame, giving one edge time series per region pair (upper triangle). Use it for edge-centric functional connectivity analyses; the time average of the edge time series equals the Pearson correlation. The README says the output is an HTML report, but the code writes a compressed TSV of edge time series with a JSON of region-pair names.

| | |
|---|---|
| 📥 **Inputs** | `generic/timeseries` |
| 📤 **Outputs** | `generic/timeseries` |
| 🐳 **Container** | `filsilva/cxnetwork:0.2.0` |
| ⚙️ **Resources** | 1 CPUs · 6 GB memory · 1 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.489](https://doi.org/10.25663/brainlife.app.489) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `ts` | `generic/timeseries` (time series) | yes | Regional fMRI time series as a TSV (time points in rows, regions in columns) with its JSON sidecar. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `generic/timeseries` | Edge time series (timeseries.tsv.gz, one column per region pair) and timeseries.json naming each pair. |

📚 **References used by this App:**
- Faskowitz J, Esfahlani FZ, Jo Y, Sporns O, Betzel RF. Edge-centric functional network representations of human cerebral cortex reveal overlapping system-level architecture. Nat Neurosci 23(12):1644-1654 (2020).
- Esfahlani FZ, Jo Y, Faskowitz J, Byrge L, Kennedy DP, Sporns O, Betzel RF. High-amplitude cofluctuations in cortical activity drive functional connectivity. PNAS 117(45) (2020).

<!-- brainlife-app:end -->

Brainlife App for creating edge time series from regional fMRI time series. Edge time series is calculated as the dot product of z-scored regional fMRI time series. 
### Authors
- [Farnaz Zamani Esfahlani]

<!-- ### Contributors
- [Richard F. Betzel]
- [Franco Pestilli]
- [Filipi Nascimento Silva]

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.-->

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
1. Faskowitz, J., Esfahlani, F. Z., Jo, Y., Sporns, O., & Betzel, R. F. (2020). Edge-centric functional network representations of human cerebral cortex reveal overlapping system-level architecture. Nature neuroscience, 23(12), 1644-1654.

2. Esfahlani, F. Z., Jo, Y., Faskowitz, J., Byrge, L., Kennedy, D. P., Sporns, O., & Betzel, R. F. (2020). High-amplitude cofluctuations in cortical activity drive functional connectivity. Proceedings of the National Academy of Sciences, 117(45), 28393-28401.


<!-- 3. Costa, L. da F., Francisco A. Rodrigues, Gonzalo Travieso, and Paulino Ribeiro Villas Boas. "Characterization of complex networks: A survey of measurements." Advances in physics 56, no. 1 (2007): 167-242.[https://doi.org/10.1080/00018730601170527](https://doi.org/10.1080/00018730601170527) -->

## Running the App 

<!-- ### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.435](https://doi.org/10.25663/brainlife.app.435) via the "Execute" tab. -->

### Running Locally (on your machine)
Singularity is required to run the package locally.

1. git clone this repo.

```bash
git clone <repository URL>
cd <repository PATH>
```

2. Inside the cloned directory, edit `config-sample.json` with your data or use the provided data.

3. Rename `config-sample.json` to `config.json` .

```bash
mv config-sample.json config.json
```

4. Launch the App by executing `main`

```bash
./main
```

### Sample Datasets

A sample dataset is provided in folder `data` and `config-sample.json`

## Output

The output is a HTML report with figures in PDF and PNG.

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install the python packages defined in `environment.yml`, then you can run the code directly from python using:  

```bash
./main.py config.json
```

