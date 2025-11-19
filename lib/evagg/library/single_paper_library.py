import logging
from typing import Any, Dict, Sequence

from lib.evagg.interfaces import IGetPapers
from lib.evagg.ref import IPaperLookupClient
from lib.evagg.types import Paper

logger = logging.getLogger(__name__)


class SinglePaperLibrary(IGetPapers):
    """A class for fetching a specific set of papers from pubmed."""

    def __init__(
        self,
        paper_client: IPaperLookupClient,
    ) -> None:
        self._paper_client = paper_client

    def get_papers(self, pmid: str) -> Sequence[Paper]:
        return [self._paper_client.fetch(pmid, include_fulltext=True)]
