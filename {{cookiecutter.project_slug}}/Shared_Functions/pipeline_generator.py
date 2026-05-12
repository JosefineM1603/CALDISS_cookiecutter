from pathlib import Path
import argparse


def to_capital_snake_case(text: str) -> str:
    return "_".join(word.capitalize() for word in text.strip().split())


def to_snake_case(text: str) -> str:
    return "_".join(word.lower() for word in text.strip().split())


def create_pipeline(name: str) -> None:
    folder_name = to_capital_snake_case(name)
    file_name = to_snake_case(name)

    pipeline_path = Path("Pipelines") / folder_name
    pipeline_path.mkdir(parents=True, exist_ok=True)

    script_path = pipeline_path / f"{file_name}.py"
    script_path.write_text(f'"""Pipeline: {folder_name}."""\n')

    print(f"Created pipeline: {pipeline_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pipeline_name", nargs="+")

    args = parser.parse_args()
    pipeline_name = " ".join(args.pipeline_name)

    create_pipeline(pipeline_name)


if __name__ == "__main__":
    main()