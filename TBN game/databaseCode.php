<?php

	// Create server variables
    $servername = "localhost";
	$username = "username";
	$password = "password";
	
	
	// Create a connection
	$conn = mysqli_connect($servername, $username, $password);
	
	// Check connection
	if(!$conn)
	{
		die("Connection failed: " .mysqli_connect_error());
		exit();
	}
	
	// Create array that will hold the question ID
	$_qarray = array[];
	
	// Keep connection open to access questions from database
	while($conn)
	{
		
		// Randomly select a question from the database
		$sql = "Select qID FROM QuestionsTable WHERE (RAND()*MAX(id)) ORDER BY RAND()
			LIMIT 1";
		$result = mysqli_query($conn, $sql);
		
		// Fetch the row associated with the question ID
		$row = mysqli_fetch_assoc($result);

		// If the questionhasn't then it will store the id and echo the result
		while(array_search($row ,$_qarray))
		{
			$sql = "Select qID FROM QuestionsTable WHERE (RAND()*MAX(id)) ORDER BY RAND()
			LIMIT 1";
			$result = mysqli_query($conn, $sql);
			$row = mysqli_fetch_assoc($result);
		}
		
		// Once it falls out of the loop, add it to the array
		array_push($_qarray, $row);
		
		// Display the question String
		print $row["qString"]."<br />";
		
		//If the category is multiple choice, put them as radio buttons
		if($row["qCat"] == "Multiple-Choice")
		{
			// Display each answer associated with the question
			if($row["option1"] != "NULL") 
			{ 
				$option_1='unchecked';
				// TODO: Display Radio Button
				echo "<table><tr><td>" $row["option1"] "</td></tr>";
			}
			if($row["option2"] != "NULL") 
			{ 
				$option_2='unchecked';
				// TODO: Display radio button
				echo "<tr><td>" $row["option2"] "</td></tr>";
			}
			if($row["option3"] != "NULL") 
			{ 
				$option_3='unchecked';
				// TODO: Display radio button
				echo "<tr><td>" $row["option3"] "</td></tr>";
			}
			if($row["option4"] != "NULL") 
			{ 
				$option_4='unchecked';
				// TODO: Display radio button
				echo "<tr><td>" $row["option4"] "</td></tr>";
			}
			if($row["option5"] != "NULL")
			{ 
				$option_5='unchecked';
				// TODO: Display radio button
				echo "<tr><td>" $row["option5"] "</td></tr>";
			}
			echo "</table>";
		}
		else
		{
			// Display a text box
			$var = 'user value';
			echo '<input type="text" name="answ1" '.$var.'">';
		}
		
		if(isset($_POST['Submit1']))
		{
			// Get answer selected from page
			$answer = $_POST['answer'];

			
			// Compare the selected answer to the correct one from the database
			if($answer == $row['correctAns')
			{ 
				echo "Correct! <br />"; 
			}
			else 
			{ 
				echo "Correct Answer: " $row['correctAns'] ."<br />"; 
			}

		}
		
		
		// Display to user why a certain answer was correct
		echo "Explanation: " $row['reason'] ."<br />";
		
		
		// Check to make sure it is still connected to the database
		mysqli_ping($conn);
		
	}
	
	// Close the connection once done or connection is lost
	mysqli_close($conn);

?>