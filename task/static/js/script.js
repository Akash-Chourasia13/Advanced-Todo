$(document).ready(function () {
	$("#addBtn").click(function () {
		fd = { task: $("#input").val() };
		$.ajax({
			url: "addTask/",
			method: "POST",
			dataType: "json",
			contentType: "application/json",
			data: JSON.stringify(fd),
			success: function (data) {
				console.log("Task added successfully");
			},
			error: function (xhr, status, error) {
				console.log("Error adding task:", error);
			},
		});
	});
});
