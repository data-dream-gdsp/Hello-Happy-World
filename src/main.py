import argparse
from rich.console import Console
from rich.prompt import Prompt
from AI.model import LLM
import requests

console = Console()

def search_duckduckgo(query, max_results=3):
    url = f"https://duckduckgo-api.vercel.app/search?q={query}&max_results={max_results}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        results = [result['snippet'] for result in data['results'][:max_results]]
        return "\n".join(results)
    else:
        console.print(f"[bold red]Error:[/bold red] Failed to fetch data from DuckDuckGo (status code: {response.status_code})")
        return None

def print_logo():
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

def make(task_type, file_name, topic=None):
    m_LLM = LLM('AI/config.yaml')
    
    if task_type == "LoRA":
        console.print(f"Generating LoRA datasets and saving to [bold green]{file_name}[/bold green]...")
        with open(file_name, 'w') as f:
            with open('static/LoRA/prompt.md', 'r') as prompt_file:
                prompt = prompt_file.read()

                if topic:
                    search_results = search_duckduckgo(topic)
                    if search_results:
                        prompt = prompt.replace("{data}", search_results)
                
                response = m_LLM.ask(prompt)
                f.write(response)
        console.print("Finish!")

    elif task_type == "SFT":
        console.print(f"Generating SFT question sets and saving to [bold green]{file_name}[/bold green]...")
        with open(file_name, 'w') as f:
            with open('static/SFT/prompt.md', 'r') as prompt_file:
                prompt = prompt_file.read()

                if topic:
                    search_results = search_duckduckgo(topic)
                    if search_results:
                        prompt = prompt.replace("{data}", search_results)
                
                response = m_LLM.ask(prompt)
                f.write(response)
        console.print("Finish!")

    else:
        console.print("[bold red]Error:[/bold red] Invalid task type.")

def cli_mode():
    parser = argparse.ArgumentParser(description="Generate LoRA datasets or SFT question sets.")
    
    parser.add_argument('--task', type=str, choices=['LoRA', 'SFT'], help="Choose between 'LoRA' datasets or 'SFT' question sets.")
    parser.add_argument('--output', type=str, help="Specify the output file name.")
    parser.add_argument('--topic', type=str, help="Search topic for generating content (optional).")

    args = parser.parse_args()
    
    if args.task and args.output:
        return args.task, args.output, args.topic
    return None, None, None

def main():
    print_logo()

    task, output_file_name, topic = cli_mode()

    if not task or not output_file_name:
        task = Prompt.ask("Do you want to generate [bold]LoRA datasets[/bold] or [bold]SFT questions sets[/bold]?", choices=["LoRA", "SFT"])
        output_file_name = Prompt.ask("What is the output file name?")

    make(task, output_file_name, topic)

if __name__ == "__main__":
    main()
