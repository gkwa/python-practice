test: wwwdev5.xml
	python t.py

wwwdev5.xml: wwwdev5.xml.xz
	xz -q -d -c wwwdev5.xml.xz >wwwdev5.xml

clean:
	rm -f wwwdev5.xml
	rm -f out.csv
