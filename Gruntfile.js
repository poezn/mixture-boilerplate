module.exports = function(grunt) {


    // Project configuration.
    grunt.initConfig({
	    "sass": {                                 // Task
	      "dist": {
            "files": {                        // Dictionary of files
                "css/custom.css": "css/custom.scss"     // 'destination': 'source'
            }
          }
	    },
		"concat": {
		  "css": {
		    "src": ['css/normalize.min.css', 'css/bootstrap.min.css', 'css/bootstrap-theme.min.css', 'css/custom.css'],
		    "dest": 'css/styles.css'
		  }
		},
		"cssmin": {
		  "css": {
		    "src": 'css/styles.css',
		    "dest": 'css/styles.min.css'
		  }
		}
    });

	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-sass');
	grunt.loadNpmTasks('grunt-contrib-cssmin');
	grunt.registerTask('default', ["sass", "concat", "cssmin"]);

};



