# RHEA-GO Mapping LLM Analysis

This repo is for tracking the analysis of the mappings between GO and RHEA using LLMs.

Note this repo follows a generic templated structure, in future it may be more customized for the GO use case

## Background

GO maps to RHEA for leaf node reactions. RHEA and GO also mutually map to other databases.

In principle the mappings between GO and RHEA should mean "equivalent" (or we refine mappings to be broad/narrow, etc).

## Approach

We ran the OAK `validate-mappings` command on the GO-RHEA mappings through a variety of different LLMs:

- GPT-4
- GPT-4-turbo
- GPT-3.5-turbo
- Claude-opus
- Gemini-Pro
- Mixtral (via Groq)
- Llama2 (via Groq)
- Mixtral-Large

In some cases API responses we too flaky, so any that yielded < 100 results were dropped.

See [How to use LLMs in OAK](https://incatools.github.io/ontology-access-kit/howtos/use-llms) for details on `validate-mappings`

## Results

https://docs.google.com/spreadsheets/d/1yFD24UT_Bc76mbwAie65KQEqfEVVIeFljrUy0HpHhNI/edit#gid=293565601