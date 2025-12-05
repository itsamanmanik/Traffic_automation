# Windows Installation Guide

This guide explains how to set up ScenarioNet / Traffic_automation on **Windows** using Conda.

## 1. Prerequisites

- Windows 10 or later
- [Anaconda](https://www.anaconda.com/products/distribution) or Miniconda installed
- Git installed (`git --version` should work in a terminal)
- (Recommended) A GPU-compatible NVIDIA driver if you plan to use GPU

> Make sure you can run `conda` and `git` from **Anaconda Prompt** or **PowerShell**.

## 2. Clone the repositories

Open **Anaconda Prompt** and run:

```bash
cd path\to\your\projects

git clone https://github.com/metadriverse/metadrive.git
git clone https://github.com/itsamanmanik/Traffic_automation.git
