# Hello-Happy-World

Hello-Happy-World is an AI-powered automatic dataset creation tool that supports generating LoRA datasets and SFT question sets from the web.

## Features

- Automatic LoRA Dataset Generation: Generate LoRA datasets using pre-defined prompts.
- Automatic SFT Question Set Generation: Create SFT question sets from prompt files.
- DuckDuckGo Search Integration: Search specific topics via DuckDuckGo, and inject search results into the generated content.

## Installation

Ensure you have installed the necessary libraries, such as `requests` and `rich`:

```bash
pip install requests rich
```

## Usage

```bash
python main.py --task [LoRA/SFT] --output [output_file_name] --topic [search_topic]
```

- `--task`: Choose the type of generation, either `LoRA` or `SFT`.
- `--output`: Specify the output file name.
- `--topic`: Specify the topic for DuckDuckGo search. The search results will replace the `{data}` placeholder in the prompt file.

## Examples

Generate an SFT question set, search for the topic "AI trends" on DuckDuckGo, and save it to `sft_output.json`:

```bash
python main.py --task SFT --output sft_output.json --topic "AI trends"
```

## File Structure

- `static/LoRA/prompt.md`: Prompt file for generating LoRA datasets.
- `static/SFT/prompt.md`: Prompt file for generating SFT question sets.
- `AI/config.yaml`: Configuration file for the LLM model.

## License

This project is licensed under the [Apache License](LICENSE). For more details, see the LICENSE file.
