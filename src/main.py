from rich.console import Console
from rich.prompt import Prompt

console = Console()

console.print(r"""
[bold blue]
  __    __     _______   ___        ___           ______          __    __         __         _______      _______    ___  ___       __   __  ___     ______      _______    ___        ________   
 /" |  | "\   /"     "| |"  |      |"  |         /    " \        /" |  | "\       /""\       |   __ "\    |   __ "\  |"  \/"  |     |"  |/  \|  "|   /    " \    /"      \  |"  |      |"      "\  
(:  (__)  :) (: ______) ||  |      ||  |        // ____  \      (:  (__)  :)     /    \      (. |__) :)   (. |__) :)  \   \  /      |'  /    \:  |  // ____  \  |:        | ||  |      (.  ___  :) 
 \/      \/   \/    |   |:  |      |:  |       /  /    ) :)      \/      \/     /' /\  \     |:  ____/    |:  ____/    \\  \/       |: /'        | /  /    ) :) |_____/   ) |:  |      |: \   ) || 
 //  __  \\   // ___)_   \  |___    \  |___   (: (____/ //       //  __  \\    //  __'  \    (|  /        (|  /        /   /         \//  /\'    |(: (____/ //   //      /   \  |___   (| (___\ || 
(:  (  )  :) (:      "| ( \_|:  \  ( \_|:  \   \        /       (:  (  )  :)  /   /  \\  \  /|__/ \      /|__/ \      /   /          /   /  \\   | \        /   |:  __   \  ( \_|:  \  |:       :) 
 \__|  |__/   \_______)  \_______)  \_______)   \"_____/         \__|  |__/  (___/    \___)(_______)    (_______)    |___/          |___/    \___|  \"_____/    |__|  \___)  \_______) (________/  
                                                                                                                                                                                                   
[/bold blue]
""", justify="center")

task = Prompt.ask("Do you want to generate [bold]LoRA datasets[/bold] or [bold]SFT questions sets[/bold]?", choices=["LoRA", "SFT"])

output_file_name = Prompt.ask("What is the output file name?")

def make(task_type, file_name):
    if task_type == "LoRA":
        console.print(f"Generating LoRA datasets and saving to [bold green]{file_name}[/bold green]...")
    elif task_type == "SFT":
        console.print(f"Generating SFT question sets and saving to [bold green]{file_name}[/bold green]...")

make(task, output_file_name)
