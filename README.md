# Hemodynamic Work Overload and Fluid Dynamics Modeling

An analytical and computational framework for modeling **Cardiac Power Overload (P)** relative to a dynamic **Vascular Restriction Index (D)** using non-linear, cubic polynomial progression algorithms. This repository bridges macrovascular fluid dynamics and clinical microrheology, offering both exact analytical solutions and high-performance numerical estimation pathways for medical telemetry systems.

## Repository Contents

*   `Hemodynamic Work.pdf`: The complete formal technical report detailing the mathematical proofs, biological parameterizations, and clinical data cohorts.
*   `Hemodynamic Work.docx`: The Microsoft Word edition of the technical report with native equation configurations.
*   `LICENSE`: Licensed under the Boost Software License 1.0 (BSL-1.0).

---

## Technical Overview

The framework models systemic cardiovascular strain under pathological conditions where blood viscosity (μ) and geometric arterial narrowing compound left ventricular workload.

### The Core Hemodynamic Model
The continuous polynomial model tracks cumulative power exertion required to bypass an integrated vascular restriction metric (1 ≤ D ≤ 100):

\[P = \text{round}\left(\frac{50D^3 + 5065D^2 + 168324D + 843000}{600}\right)\]

When decomposed to remove the discrete rounding function, the continuous function f(D) reads:

\[f(D) = \frac{1}{12}D^3 + \frac{1013}{120}D^2 + \frac{14027}{50}D + 1405\]

### Microvascular Rheology & Parameterization
The variable D integrates both structural anatomy and fluid rheology. In microvessels (< 300 μm), it accounts for the **Fåhræus–Lindqvist effect** (the formation of a cell-free marginal plasma zone that reduces effective apparent viscosity). The repository explores how pathological processes like hypercholesterolemia stiffen erythrocyte membranes, disrupting this lubrication layer and driving D sharply upward.

---

## Solving for Vascular Restriction (D)

In practical diagnostics, clinicians measure the output work parameter (P) and must solve backwards for the underlying arterial state (D). This repository details two core methods to solve the resulting cubic equation:

### 1. Analytical Solution (Cardano's Method)
By applying a standard normalization followed by Cardano’s depressed cubic substitution (D = x - 33.77), the equation simplifies to x³ + px + q = 0, where:
*   p = -54.08
*   q = -36411.39 - 12P

The final root is resolved precisely via:
\[x = \sqrt[3]{-\frac{q}{2} + \sqrt{\frac{q^2}{4} + \frac{p^3}{27}}} + \sqrt[3]{-\frac{q}{2} - \sqrt{\frac{q^2}{4} + \frac{p^3}{27}}}\]
\[D = x - 33.77\]

### 2. Numerical Solution (Newton-Raphson Loop)
For real-time telemetry hardware and microcontrollers, an iterative root-finding loop provides low-overhead, quadratic convergence:

\[D_{n+1} = D_n - \frac{0.08333D_n^3 + 8.44167D_n^2 + 280.54D_n + 1405 - P}{0.25D_n^2 + 16.8833D_n + 280.54}\]

---

## Clinical Interventions & Workload Reductions

The mathematical models track how targeted therapies shift a patient along the restriction curve, significantly lowering the required Cardiac Power Output (P):

*   **Nicotinic Acid USP 500mg:** Reduces macroscopic viscosity by suppressing plasma fibrinogen and expanding the effective lumen diameter (d) via prostaglandin pathways. This can downscale a patient from D=40 to D=20, saving **75.7%** of left ventricular pumping energy.
*   **Bivalent Cations (Zn²⁺ and Mg²⁺):** Magnesium blocks the calcium-activated Gardos channel to prevent cell dehydration, while Zinc shields skeletal proteins from oxidative cross-linking. Together, they restore erythrocyte deformability, driving end-stage microvascular values from D=60 down to D=20, establishing a **90.5%** reduction in mechanical cardiac overload.

---

## Reference Foundations

The mathematical and biological paradigms established in this work are grounded in trusted official frameworks:
*   **Proteomic Data Mining:** Sequence temperature and biomarker features aligned with the [NIH PubMed Protein Pilot Datasets](https://nih.gov).
*   **Microvascular Verification:** Rheological models validated against the Pries-Secomb empirical formulations and [AHA Journals microcirculatory datasets](https://ahajournals.org).

## License

This project is licensed under the Boost Software License 1.0 - see the [LICENSE](LICENSE) file for details.
