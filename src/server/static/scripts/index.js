$(function(){
	
	var maps = [];
	var mapCount = 4;
	
	for (var i=1;i<=mapCount;i++){
		google.earth.createInstance('map'+i, function(instance) {
			var ge = instance;
			ge.getWindow().setVisibility(true);
			ge.getNavigationControl().setVisibility(ge.VISIBILITY_AUTO);
			var options = ge.getOptions();
			options.setStatusBarVisibility(true);
			options.setScaleLegendVisibility(true);
			options.setOverviewMapVisibility(true);
			maps.push(ge);
		},
		function(errorCode){
			alert(errorCode);
		});	
	}
	var ws = new WebSocket("ws://localhost:8888/socket");
	ws.onmessage = function(event) {
		var data = jQuery.parseJSON(event.data);
		var lat = data["lat"];
		var lon = data["lon"];
		
		if (lat != undefined && lon != undefined) {
			for (var n=mapCount - 1;n>=0;n--){
				var map = maps[n];
				var lookAt = map.getView().copyAsLookAt(map.ALTITUDE_RELATIVE_TO_GROUND);
				lookAt.setTilt(30);
				lookAt.setLatitude(lat);
				lookAt.setLongitude(lon);
				lookAt.setHeading(90 * n);
				lookAt.setAltitude(0);
				lookAt.setRange(1500);
				map.getView().setAbstractView(lookAt);
			}
		}
	};
});
