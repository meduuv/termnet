# TermNet

> A terminal-first view of local network state.

TermNet is a lightweight network dashboard for inspecting local connections, endpoints, and traffic snapshots from the terminal.

## Highlights

- Terminal-oriented network visibility
- Local connection and endpoint inspection
- Snapshot-based diagnostics
- Read-only operation
- Designed for machines you administer

## Usage

```bash
termnet
termnet --json
```

## Workflow

```text
local network state
        ↓
   collect snapshot
        ↓
    summarize data
        ↓
 terminal / JSON view
```

## Use Cases

- Network troubleshooting
- Local endpoint visibility
- Development diagnostics
- Defensive monitoring prototypes
- Terminal-based system tooling

## Safety

TermNet is an inspection utility. It does not modify connections, inject traffic, or perform unauthorized network actions.

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
