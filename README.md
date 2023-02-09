# Advent of Code 2022

Repository for my attempt at the Advent of Code.

Each day is contained in its own folder, with scripts common to different tasks stored in a separate folder.

## Python

A tools folder is included with some reusable scripts.
To include these, "*path/to/*AdventOfCode22" must be added to the `$PYTHONPATH` environment variable.

To import the scripts, use either:

``` python
    import tools.[scriptname] (as [alias])
```

``` python
    from tools import [scriptname] (as [alias])
```

Python files can be run from within VS code's editor,
or by running the following in the terminal:

```cmd
    python dayXX/dayXX.py
```

## Go

Go files can be run from the terminal with the following:

```cmd
    go run dayXX/dayXX.go
```
