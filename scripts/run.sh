echo Start generating Python

#2: Run generate and run tests
cd "$1" || { echo '020' ; exit 1; }
/usr/bin/haxe buildtests.hxml || { echo '030' ; exit 1; }
python "$1/munge_haxe_python3_to_python2.py" < "$1/sUTLHaxePython2/hxsUTLTests3.py" > "$1/sUTLHaxePython2/hxsUTLTests2.py" || { echo '040' ; exit 1; }
rm "$1/sUTLHaxePython2/hxsUTLTests3.py" || { echo '042' ; exit 1; }
python "$1/sUTLHaxePython2/hxsUTLTests2.py" || { echo '045' ; exit 1; }

#3: Generate the python interpreter
/usr/bin/haxe build.hxml || { echo '050' ; exit 1; }
python "$1/munge_haxe_python3_to_python2.py" < "$1/sUTLHaxePython2/hxsUTL3.py" > "$1/sUTLHaxePython2/hxsUTL2.py" || { echo '055' ; exit 1; }
rm "$1/sUTLHaxePython2/hxsUTL3.py" || { echo '057' ; exit 1; }

echo Finished generating Python