import sys
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt, Prompt
from rich.panel import Panel

from src.tracker import FitnessTracker
from src.models import WorkoutLog

console = Console()

class CLIApp:
    """
    Interactive Command Line Interface for the Fitness Tracker.
    """
    def __init__(self):
        self.tracker = FitnessTracker()

    def display_menu(self) -> None:
        """Renders the main menu panel."""
        menu_text = (
            "[1] Log Today's Workout\n"
            "[2] View Logging History\n"
            "[3] Exit"
        )
        console.print(Panel(menu_text, title="[bold cyan]Main Menu[/bold cyan]", border_style="cyan", expand=False))

    def log_workout(self) -> None:
        """Handles user input for logging daily metrics."""
        console.print("\n[bold yellow]Record your metrics for today:[/bold yellow]")
        try:
            pushups = IntPrompt.ask("Total Pushups")
            plank_sec = IntPrompt.ask("Plank Duration (seconds)")
            
            # Validate 6-day split input
            split_day = 0
            while split_day not in range(1, 7):
                split_day = IntPrompt.ask("Gym Split Day (1-6)")
                if split_day not in range(1, 7):
                    console.print("[red]Invalid split day. Please enter a number between 1 and 6.[/red]")

            log = WorkoutLog.create(pushups, plank_sec, split_day)
            
            if self.tracker.save_log(log):
                console.print("[bold green]✔ Workout logged successfully![/bold green]\n")
            else:
                console.print("[bold red]✖ Failed to save the workout.[/bold red]\n")

        except KeyboardInterrupt:
            console.print("\n[red]Logging cancelled.[/red]")

    def view_stats(self) -> None:
        """Retrieves and displays historical logs in a formatted table."""
        logs = self.tracker.load_logs()
        
        if not logs:
            console.print("[yellow]No workout logs found. Start training![/yellow]\n")
            return

        table = Table(title="Workout History", header_style="bold magenta", border_style="magenta")
        table.add_column("Date", style="cyan")
        table.add_column("Pushups", justify="right", style="green")
        table.add_column("Plank (s)", justify="right", style="yellow")
        table.add_column("Split Day", justify="center", style="blue")

        for log in logs:
            # Format the ISO timestamp into a cleaner string
            date_obj = datetime.fromisoformat(log.timestamp)
            date_str = date_obj.strftime("%Y-%m-%d %H:%M")
            
            table.add_row(
                date_str,
                str(log.pushups),
                str(log.plank_duration_sec),
                str(log.gym_split_day)
            )

        console.print(table)
        console.print() # Empty line for spacing

    def run(self) -> None:
        """Main execution loop for the CLI."""
        console.clear()
        console.print("[bold cyan]=== CLI Fitness & Habit Logger ===[/bold cyan]\n")
        
        while True:
            self.display_menu()
            choice = Prompt.ask("Choose an option", choices=["1", "2", "3"])
            
            if choice == "1":
                self.log_workout()
            elif choice == "2":
                self.view_stats()
            elif choice == "3":
                console.print("[bold cyan]Keep up the great work! Goodbye.[/bold cyan]")
                sys.exit(0)

if __name__ == "__main__":
    app = CLIApp()
    app.run()