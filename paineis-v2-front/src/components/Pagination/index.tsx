import classnames from 'classnames';
import { usePagination, DOTS } from '../../utils/usePagination';
import './style.scss';

type Props = {
  onPageChange: (p: any) => void;
  totalCount: number;
  siblingCount?: number;
  currentPage: any;
  pageSize: number;
  className: any;
};

const Pagination = ({
  onPageChange,
  totalCount,
  siblingCount = 1,
  currentPage,
  pageSize,
  className,
}: Props) => {
  const paginationRange = usePagination({
    currentPage,
    totalCount,
    siblingCount,
    pageSize,
  });

  if (currentPage === 0 || (paginationRange && paginationRange.length < 2)) {
    return null;
  }

  const onNext = () => {
    onPageChange(currentPage + 1);
  };

  const onPrevious = () => {
    onPageChange(currentPage - 1);
  };

  const lastPage =
    paginationRange && paginationRange[paginationRange.length - 1];

  return (
    <ul
      className={classnames('pagination-container', { [className]: className })}
    >
      <li
        className={classnames('pagination-item', {
          disabled: currentPage === 1,
        })}
        onClick={onPrevious}
      >
        <div className='arrow left' />
      </li>

      {paginationRange?.map((pageNumber: any, i: number) => {
        if (pageNumber === DOTS) {
          return (
            <li key={i} className='pagination-item dots'>
              &#8230;
            </li>
          );
        }

        return (
          <li
            key={i}
            className={classnames('pagination-item', {
              selected: pageNumber === currentPage,
            })}
            onClick={() => onPageChange(pageNumber)}
          >
            {pageNumber}
          </li>
        );
      })}
      <li
        className={classnames('pagination-item', {
          disabled: currentPage === lastPage,
        })}
        onClick={onNext}
      >
        <div className='arrow right' />
      </li>
    </ul>
  );
};

export default Pagination;
