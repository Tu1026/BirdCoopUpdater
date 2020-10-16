@echo off
call activate tracker
cd %~dp0
call python updateScript.py

